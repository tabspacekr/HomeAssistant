#!/usr/bin/env python

# 마그네틱방식 출입제어기 v7
# 2022.04.20. ceo@tabspace.kr
# MagTek MSR100 Mini Swipe Card Reader, Sonoff RE5V1C 필요
# 사전에 pymysql, pyusb를 pip3로 설치 필요함

import usb.core
import usb.util
import pymysql.cursors
import requests
import os 
import time
import sys
import json
from requests import get

# 이곳에 사이트명과 엔티티명을 입력
ha_site = "your.ha.url"
ha_entity = "test01" # alarm_control_panel 뒷부분만 입력
device_id = "TEST01"
bypass = 0
relay_ip = "192.168.88.100"

# 이곳에 릴레이 URL을 입력
#relay_url = "http://192.168.1.119/cm?cmnd=Power%20off" # Sonoff RE5V1C에서 할당받은 ip주소로 변경이 필요. mac주소 고정 권장
# 만약 ID가 admin 비밀번호가 joker 형태로 설정되어 있으면
#relay_url = "http://192.168.88.100/cm?user=admin&password=jocker&cmnd=Power%20off"
relay_url = "http://"+relay_ip+"/cm?user=admin&password=jocker&cmnd=Power%20off"

# 이곳에 마그네틱리더기 vendorid 및 productid값 입력
# 리눅스 콘솔에서 lsusb를 입력하여, 인식된 키보드 에뮬레이션 방식의 카드리더기의 Bus 정보와 Device 정보를 입력해주어야함
# MagTek Device MSR100 Mini Swipe : Bus 006 Device 002: ID 0801:0001 MagTek Mini Swipe Reader (Keyboard Emulation)
# Unlabeled MSR100 Like Device : Bus 001 Device 005: ID ffff:0035 
# Bus 006 Device 002: ID 0801:0001 MagTek Mini Swipe Reader (Keyboard Emulation)
vendorid = 0x0801
productid = 0x0001
# Bus 001 Device 005: ID ffff:0035 Unlabeled MSR100 Like Device 
#vendorid = 0xffff
#productid = 0x0035

ha_url = "https://"+ha_site+"/api/states/alarm_control_panel."+ha_entity

if ha_site == "your.ha.url":
    ha_headers = {
    "Authorization": "Bearer ABCDEFG",
    "content-type": "application/json",
    }
elif ha_site == "your.another.ha.url":
    ha_headers = {
    "Authorization": "Bearer ABCDEFG",
    "content-type": "application/json",
    }
elif ha_site == "your.other.ha.url":
    ha_headers = {
    "Authorization": "Bearer ABCDEFG",
    "content-type": "application/json",
    }

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

# 사전 지정된 마그네틱 리더기의 디바이스 ID를 검색하여, 존재하지 않는 경우 종료처리
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
#finally:
#    os.system('reboot') # 원인모를 오류 발생 시에 리부팅함
# usb.core.USBError: [Errno None] Other error 가 나더라도, 카드를 몇번 읽다보면 동작하기때문에 reboot까지는 하지않음.
# reboot을 넣고나니 무한정 재부팅되는 이슈가 있음. 최초1번만이라도 카드를 긁으면 정상적으로 인식됨.

# get device endpoint information
endpoint = device[0][(0,0)][0]

# 2회 이상 카드 읽기가 실패한 경우, 3회째에 출입허용 하기 위한 카운팅 변수 선언
errorcount = 0

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
    #print(sdata[1])
    #print(len(sdata)
    #if(len(sdata)<100): # 파싱한 데이터가 100보다 작을 경우에 종료하는 형태로 최초 구성하였으나, 정상적으로 읽은 값 처리가 가능하여 주석처리함
    #    print('error')
    #    continue
    
    # sdata의 2번째 배열은 정상값일 경우 B로 인식되며, 에러값일 경우 E로 인식됨. 이에따라 B가 아닌 경우는 에러카운트를 늘려주고 다시 시도하도록 continue처리
    if sdata[1] not in 'B':
        if errorcount >= 2: # 에러카운트가 2이상인 경우에는, 에러카운트를 0으로 리셋한 후 문열림 진행 처리함
            print('Bypass!')
            errorcount = 0
            bypass = 1
        else: # 에러출력 후, 음성안내하고 에러카운트를 1증가 후 다시 반복문 진행
            print('Error!')
            try:
                # 마그네틱 카드 정보를 db에 insert하기 위한 connection 정보
                conn = pymysql.connect(
                    host = 'your.database.url', # host name
                    user = 'db_user_name', # user name
                    password = 'db_user_password', # password
                    db = 'db_name', # db name
                    charset = 'utf8mb4'
                )                
                # DB접속
                print ("Error Log : DB Connection Start")
                cursor = conn.cursor()
                # mgreader_log 테이블에 device_id와 mg_data insert
                sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);"
                val = (device_id, "__FAIL_"+sdata)
                cursor.execute(sql, val)
                conn.commit()
                conn.close()
                print ("Error Log : DB Connection End") 
            except pymysql.err.InternalError as e:
                code, msg = e.args
            os.system("mpg123 -q " + "/root/error.mp3")
            errorcount = errorcount + 1
            continue
    errorcount = 0 # 정상진행된 경우 에러카운트를 0으로 리셋함


    ha_response = get(ha_url, headers=ha_headers)
    #print(response.text)
    #j = json.loads(response.text)
    #print(j["state"])

    ha_lock_state = json.loads(ha_response.text)["state"]
    # ha_lock_state : disarmed (항시개방), armed_away(경비중-신용카드긁으면문은열림), armed_custom_bypass(경비중-카드키반응안함)
    print("Current HA Lock State = ["+ha_lock_state+"]")

    if ha_lock_state == "armed_custom_bypass":
        print("Door Open Block by Admin!!!")
        try:
            # 마그네틱 카드 정보를 db에 insert하기 위한 connection 정보
            conn = pymysql.connect(
                host = 'your.database.url', # host name
                user = 'db_user_name', # user name
                password = 'db_user_password', # password
                db = 'db_name', # db name
                charset = 'utf8mb4'
            )
            # DB접속
            print ("DB Connection Start")
            cursor = conn.cursor()
            # mgreader_log 테이블에 device_id와 mg_data insert
            sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);"
            val = (device_id, "__LOCK_"+sdata)
            cursor.execute(sql, val)
            conn.commit()
            conn.close()
            print ("DB Connection End") 
        except pymysql.err.InternalError as e:
            code, msg = e.args
        os.system("mpg123 -q " + "/root/door_close.mp3")
        continue

    #print ("OK")
    # Sonoff RE5V1C의 릴레이를 curl형태로 호출, 전원을 차단처리하여 데드볼트락의 failsafe기능으로 문이 열리는 원리임
    try:
        print("Door Open Command Start")
        door_open = requests.get(relay_url).json
        print("Door Open Command End")
    except:
        print('Door Open Failed!!')

    # to do : 마그네틱 카드 정보 로컬 파일 저장 (로깅기능이 있으므로 기능구현은 추후에 수행)
    # to do : 긁은 코드에 대해 정교하게 처리하는 방식이 필요함. 정교하게 하기 위해서는 0000 코드가 들어왔을떄에 다시 긁어달라는 내용이 필요하나, 고민이 필요한 부분이 있음.
    # -------- 위 부분은 sdata의 2번째값이 B이면 정상, E이면 에러임을 식별하여 해결하였음

    #playsound.playsound('/root/door_open.mp3')
    os.system("mpg123 -q " + "/root/door_open.mp3")
    #p = vlc.MediaPlayer("/root/door_open.mp3")
    #p.play()
    
    #bypass 상황인 경우 DB에 기록
    if bypass == 1:
        try:
            # 마그네틱 카드 정보를 db에 insert하기 위한 connection 정보
            conn = pymysql.connect(
                host = 'your.database.url', # host name
                user = 'db_user_name', # user name
                password = 'db_user_password', # password
                db = 'db_name', # db name
                charset = 'utf8mb4'
            )                
            # DB접속
            print ("Bypass Log : DB Connection Start")
            cursor = conn.cursor()
            # mgreader_log 테이블에 device_id와 mg_data insert
            sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);"
            val = (device_id, "__PASS_"+sdata)
            cursor.execute(sql, val)
            conn.commit()
            conn.close()
            print ("Bypass Log : DB Connection End") 
            bypass = 0
        except pymysql.err.InternalError as e:
            code, msg = e.args
        continue

    try:
        # 마그네틱 카드 정보를 db에 insert하기 위한 connection 정보
        conn = pymysql.connect(
            host = 'your.database.url', # host name
            user = 'db_user_name', # user name
            password = 'db_user_password', # password
            db = 'db_name', # db name
            charset = 'utf8mb4'
        )
        # DB접속
        print ("DB Connection Start")
        cursor = conn.cursor()
        # mgreader_log 테이블에 device_id와 mg_data insert
        sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);"
        val = (device_id, sdata)
        cursor.execute(sql, val) # db insert
        conn.commit() # db commit
        conn.close() # db 연결 종료
        print ("DB Connection End") 
    except:
        print('Door Open Failed!!')
