#!/usr/bin/env python

# 마그네틱방식 출입제어기 v1
# 2021.12.21. ceo@tabspace.kr
# MagTek MSR100 Mini Swipe Card Reader, Sonoff RE5V1C 필요
# 사전에 pymysql, pyusb를 pip3로 설치 필요함

import usb.core
import usb.util
import pymysql.cursors
import requests

# 리눅스 콘솔에서 lsusb를 입력하여, 인식된 키보드 에뮬레이션 방식의 카드리더기의 Bus 정보와 Device 정보를 입력해주어야함
# MagTek Device MSR100 Mini Swipe : Bus 006 Device 002: ID 0801:0001 MagTek Mini Swipe Reader (Keyboard Emulation)
# Unlabeled MSR100 Like Device : Bus 001 Device 005: ID ffff:0035 

# Bus 006 Device 002: ID 0801:0001 MagTek Mini Swipe Reader (Keyboard Emulation)
#vendorid = 0x0801
#productid = 0x0001
# Bus 001 Device 005: ID ffff:0035 Unlabeled MSR100 Like Device 
vendorid = 0xffff
productid = 0x0035


# Define our Character Map per Reference Manual
# http://www.magtek.com/documentation/public/99875206-17.01.pdf

chrMap = {
    4:  'a',
    5:  'b',
    6:  'c',
    7:  'd',
    8:  'e',
    9:  'f',
    10: 'g',
    11: 'h',
    12: 'i',
    13: 'j',
    14: 'k',
    15: 'l',
    16: 'm',
    17: 'n',
    18: 'o',
    19: 'p',
    20: 'q',
    21: 'r',
    22: 's',
    23: 't',
    24: 'u',
    25: 'v',
    26: 'w',
    27: 'x',
    28: 'y',
    29: 'z',
    30: '1',
    31: '2',
    32: '3',
    33: '4',
    34: '5',
    35: '6',
    36: '7',
    37: '8',
    38: '9',
    39: '0',
    40: 'KEY_ENTER',
    41: 'KEY_ESCAPE',
    42: 'KEY_BACKSPACE',
    43: 'KEY_TAB',
    44: ' ',
    45: '-',
    46: '=',
    47: '[',
    48: ']',
    49: '\\',
    51: ';',
    52: '\'',
    53: '`',
    54: ',',
    55: '.',
    56: '/',
    57: 'KEY_CAPSLOCK'
}

shiftchrMap = {
    4:  'A',
    5:  'B',
    6:  'C',
    7:  'D',
    8:  'E',
    9:  'F',
    10: 'G',
    11: 'H',
    12: 'I',
    13: 'J',
    14: 'K',
    15: 'L',
    16: 'M',
    17: 'N',
    18: 'O',
    19: 'P',
    20: 'Q',
    21: 'R',
    22: 'S',
    23: 'T',
    24: 'U',
    25: 'V',
    26: 'W',
    27: 'X',
    28: 'Y',
    29: 'Z',
    30: '!',
    31: '@',
    32: '#',
    33: '$',
    34: '%',
    35: '^',
    36: '&',
    37: '*',
    38: '(',
    39: ')',
    40: 'KEY_ENTER',
    41: 'KEY_ESCAPE',
    42: 'KEY_BACKSPACE',
    43: 'KEY_TAB',
    44: ' ',
    45: '_',
    46: '+',
    47: '{',
    48: '}',
    49: '|',
    51: ':',
    52: '"',
    53: '~',
    54: '<',
    55: '>',
    56: '?',
    57: 'KEY_CAPSLOCK'
}

# find our device by id
device = usb.core.find(idVendor=vendorid, idProduct=productid)
if device is None:
    raise Exception('Could not find USB Card Reader')

# remove device from kernel, this should stop
# reader from printing to screen and remove /dev/input
if device.is_kernel_driver_active(0):
    try:
        device.detach_kernel_driver(0)
    except usb.core.USBError as e:
        raise Exception("Could not detatch kernel driver: %s" % str(e))

# load our devices configuration
try:
    device.set_configuration()
    device.reset()
except usb.core.USBError as e:
    raise Exception("Could not set configuration: %s" % str(e))

# get device endpoint information
endpoint = device[0][(0,0)][0]

# 무한반복 시작
while True:
    swiped = False
    data = []
    datalist = []
    print('Swipe Card:')
    while True:
        try:
            results = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, timeout=5)
            data += results
            datalist.append(results)
            swiped = True

        except usb.core.USBError as e:
            if e.args[1] == 'Operation timed out' and swiped:
                break # timeout and swiped means we are done

    # create a list of 8 bit bytes and remove
    # empty bytes
    ndata = []
    for d in datalist:
        if d.tolist() != [0, 0, 0, 0, 0, 0, 0, 0]:
            ndata.append(d.tolist())

    # parse over our bytes and create string to final return
    sdata = ''
    for n in ndata:
        # handle non shifted letters
        if n[2] in chrMap and n[0] == 0:
            sdata += chrMap[n[2]]
        # handle shifted letters
        elif n[2] in shiftchrMap and n[0] == 2:
            sdata += shiftchrMap[n[2]]

    print (sdata)

    # to do : 마그네틱 카드 정보 로컬 파일 저장 (로깅기능이 있으므로 기능구현은 추후에 수행)
    # to do : 긁은 코드에 대해 정교하게 처리하는 방식이 필요함. 정교하게 하기 위해서는 0000 코드가 들어왔을떄에 다시 긁어달라는 내용이 필요하나, 고민이 필요한 부분이 있음.

    # 마그네틱 카드 정보를 db에 insert하기 위한 connection 정보
    conn = pymysql.connect(
        host = 'database.kr', # host name
        user = 'user_name', # user name
        password = 'pass_word', # password
        db = 'db_name', # db name
        charset = 'utf8mb4'
    )
    # DB접속
    cursor = conn.cursor()
    
    # mgreader_log 테이블에 device_id와 mg_data insert
    sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);"
    val = ("VAVAS01", sdata)
    
    # db insert
    cursor.execute(sql, val)
    # db commit
    conn.commit()
    # db 연결 종료
    conn.close()

    # Sonoff RE5V1C의 릴레이를 curl형태로 호출, 전원을 차단처리하여 데드볼트락의 failsafe기능으로 문이 열리는 원리임
    url = "http://192.168.1.119/cm?cmnd=Power%20off" # Sonoff RE5V1C에서 할당받은 ip주소로 변경이 필요. mac주소 고정 권장
    # 만약 ID가 admin 비밀번호가 joker 형태로 설정되어 있으면
    # url = "http://192.168.1.119/cm?user=admin&password=joker&cmnd=Power%20off"
    try:
      door_open = requests.get(url).json
    except:
      print('Door Open Failed!!')
