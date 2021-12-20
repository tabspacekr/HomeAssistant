#!/usr/bin/env python

# MagTek MSR100 Mini Swipe Card Reader
# Original Code Written By: Jeffrey Ness
# ReWrite Code Written By: TabSpace
# 
# Some Thanks need to go out to
# http://www.micahcarrick.com/credit-card-reader-pyusb.html
# for helping me get on the right track

import usb.core
import usb.util
import pymysql.cursors

# connection 정보
conn = pymysql.connect(
    host = 'db.yourdb', # host name
    user = 'tabspace', # user name
    password = 'yourpassword', # password
    db = 'tabspace', # db name
    charset = 'utf8mb4'
)
cursor = conn.cursor()

# MagTek Device MSR100 Mini Swipe
#enter lsusb
#Bus 006 Device 002: ID 0801:0001 MagTek Mini Swipe Reader (Keyboard Emulation)

vendorid = 0x0801
productid = 0x0001

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

    sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);"
    val = ("VAVAS01", sdata)
    #print (sql)
    cursor.execute(sql, val)
    conn.commit()

    #반복은 계속 되고 있는중. 프로세스 모니터링 하여서, 만약에 mgreader python 프로그램이 죽으면 다시 동작하게끔 하는 코드를 고려해야함.
    #로컬 텍스트 파일 및 클라우드 DB에 데이터를 쌓아야함. 순번, 시간정보와, 어디서 긁혔는지 코드정보, 데이터를 저장하는 필드가 필요함.
    #긁은 코드에 대해 정교하게 처리하는 방식이 필요함. 정교하게 하기 위해서는 0000 코드가 들어왔을떄에 다시 긁어달라는 내용이 필요하나, 고민이 필요한 부분이 있음.
    #열어주는 코드
