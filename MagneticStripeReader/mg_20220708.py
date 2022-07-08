#!/usr/bin/env python

# 마그네틱방식 출입제어기 v13
# 2022.07.08. ceo@tabspace.kr
# MagTek MSR100 Mini Swipe Card Reader, Relay 필요
# 사전에 pymysql, pyusb를 pip3로 설치 필요함

import usb.core
import usb.util
import pymysql.cursors
import requests
import os 
import sys
import time
from datetime import datetime
import json
from requests import get
import configparser
import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)         # set BCM11 as an output (RELAY)

# 환경 설정 파일 호출
config = configparser.ConfigParser()
config.read('mg.ini')

# HA 사이트와 엔티티를 환경설정파일에서 불러옴
ha_site = config.get("HA","ha_site")
ha_entity = config.get("HA","ha_entity") # input_select. 뒷부분만 입력
device_id = config.get("DB","device_id")
bypass = False
errorcount = 0
errorcount_limit = config.getint("CARD","errorcount_limit") 

# Sonoff RE5V1C 릴레이 Tasmota의 IP는 공유기에서 MAC-ADDRESS 고정하여 사용을 권장함
# relay_ip = config.get("RELAY","relay_ip")
# relay_id = config.get("RELAY","relay_id")
# relay_password_use = config.getboolean("RELAY","relay_password_use") # 릴레이 Tasmota의 비밀번호가 설정되어 있지 않은 경우 False입력
# relay_password = config.get("RELAY","relay_password")

# Relay Password 사용유무 판별하여 URL생성
# if relay_password_use == True:
#     relay_url = "http://"+relay_ip+"/cm?user="+relay_id+"&password="+relay_password+"&cmnd=Power%20off" 
# elif relay_password_use == False:
#     relay_url = "http://"+relay_ip+"/cm?cmnd=Power%20off" 

# 마그네틱리더기 vendorid 및 productid 정보 호출
vendorid = int(config.get("CARD","vendorid"), 16)
productid = int(config.get("CARD","productid"), 16)

ha_url = "https://"+ha_site+"/api/states/input_select."+ha_entity
ha_token = config.get("HA","ha_token")
ha_headers = {
    "Authorization": "Bearer "+ha_token,
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

# 리눅스 커널에서 마그네틱 리더기의 디바이스를 제거, 스크린출력 방지 및 /dev/input에서 입력장치 제거
if device.is_kernel_driver_active(0):
    try:
        device.detach_kernel_driver(0)
    except usb.core.USBError as e:
        raise Exception("Could not detatch kernel driver: %s" % str(e))

# 마그네틱 리더기 설정
try:
    device.set_configuration()
    device.reset()
except usb.core.USBError as e:
    raise Exception("Could not set configuration: %s" % str(e)) 
#finally:
#    os.system('reboot') # 원인모를 오류 발생 시에 리부팅함
# usb.core.USBError: [Errno None] Other error 가 나더라도, 카드를 몇번 읽다보면 동작하기때문에 reboot까지는 하지않음.
# reboot을 넣고나니 무한정 재부팅되는 이슈가 있음. 최초1번만이라도 카드를 긁으면 정상적으로 인식됨.

# 마그네틱 리더기 endpoint 정보를 가지고 옴
endpoint = device[0][(0,0)][0]

# 별도의 인터럽트가 없을 때까지 무한반복 시작
while True:
    swiped = False
    data = []
    datalist = []
    print("["+str(datetime.now())+"] Wait for Swipe Card...")

    # 카드 리더기로 부터 데이터 입력 대기
    while True:
        try:
            results = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, timeout=5)
            data += results
            datalist.append(results)
            swiped = True

        except usb.core.USBError as e:
            if e.args[1] == 'Operation timed out' and swiped:
                break # timeout and swiped means we are done
    print("["+str(datetime.now())+"] ")
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

    # 파싱 완료된 데이터값 출력
    print("["+str(datetime.now())+"] Card Data : "+sdata)

    # sdata의 2번째 배열은 정상값일 경우 B로 인식되며, 에러값일 경우 E로 인식됨. 이에따라 B가 아닌 경우는 에러카운트를 늘려주고 다시 시도하도록 continue처리
    # 인식이 안되는 사례는 아래와 같으며, 2번째 값이 E로 들어오는것을 확인할 수 있음.
    # %E?;E?+E?
    # %E?;E?
    # ;E?
    if sdata[1] not in 'B':
        if errorcount < errorcount_limit - 1: # 에러카운트 1증가, 에러출력 후 음성안내하고 다시 반복문 진행
            errorcount = errorcount + 1
            print("["+str(datetime.now())+"] Card Read Error! : "+str(errorcount)+"/"+str(errorcount_limit))
            try:
                # 마그네틱 카드 정보를 db에 insert하기 위한 connection 정보
                conn = pymysql.connect(
                    host = config.get("DB","db_host"), # host name
                    port = int(config.get("DB","db_port")), # db port
                    user = config.get("DB","db_user"), # user name
                    password = config.get("DB","db_password"), # password
                    db = config.get("DB","db_name"), # db name
                    charset = config.get("DB","db_charset")
                )                
                # DB접속
                print ("["+str(datetime.now())+"] Error Log : DB Connection Start")
                cursor = conn.cursor()
                # mgreader_log 테이블에 device_id와 mg_data insert
                sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);" 
                val = (device_id, "__FAIL_"+sdata)
                cursor.execute(sql, val)
                conn.commit()
                conn.close()
                print ("["+str(datetime.now())+"] Error Log : DB Connection End") 
            except pymysql.err.InternalError as e:
                code, msg = e.args
            os.system("mpg123 -q " + "/root/error.mp3")
            continue
        else: # 에러카운트가 위에서 선언한 리미트 이상인 경우에는, 에러카운트를 0으로 리셋한 후 문열림 진행 처리함
            print("["+str(datetime.now())+"] Bypass!")
            errorcount = 0
            bypass = True

    errorcount = 0 # 정상진행된 경우 에러카운트를 리셋함

    # Rest API로 HA에 lock_state를 받아옴
    ha_response = get(ha_url, headers=ha_headers)
    ha_lock_state = json.loads(ha_response.text)["state"]
    # ha_lock_state : unlock (항시개방), lock (경비중-카드긁으면문열림), lockdown(락다운-카드키반응안함)
    print("["+str(datetime.now())+"] Current HA Lock State = ["+ha_lock_state+"]")

    if ha_lock_state == "lockdown":
        print("["+str(datetime.now())+"] Door Open Block by Admin!!!")
        try:
            # 마그네틱 카드 정보를 db에 insert하기 위한 connection 정보
            conn = pymysql.connect(
                host = config.get("DB","db_host"), # host name
                port = int(config.get("DB","db_port")), # db port
                user = config.get("DB","db_user"), # user name
                password = config.get("DB","db_password"), # password
                db = config.get("DB","db_name"), # db name
                charset = config.get("DB","db_charset")
            )
            # DB접속
            print ("["+str(datetime.now())+"] Block Log : DB Connection Start")
            cursor = conn.cursor()
            # mgreader_log 테이블에 device_id와 mg_data insert
            sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);" 
            val = (device_id, "__LOCK_"+sdata)
            cursor.execute(sql, val)
            conn.commit()
            conn.close()
            print ("["+str(datetime.now())+"] Block Log : DB Connection End") 
        except pymysql.err.InternalError as e:
            code, msg = e.args
        os.system("mpg123 -q " + "/root/door_close.mp3")
        continue

    # Sonoff RE5V1C의 릴레이를 curl형태로 호출, 전원을 차단처리하여 데드볼트락의 failsafe기능으로 문이 열리는 원리임
    try:
        print("["+str(datetime.now())+"] Door Open Command Start")
        #door_open = requests.get(relay_url).json
        GPIO.output(3, 0)
        sleep(0.1)
        GPIO.output(3, 1)
        print("["+str(datetime.now())+"] Door Open Command End")
    except:
        print("["+str(datetime.now())+"] Door Open Failed!!")

    #bypass 상황인 경우 DB에 기록
    if bypass == True:
        try:
            # 마그네틱 카드 정보를 db에 insert하기 위한 connection 정보
            conn = pymysql.connect(
                host = config.get("DB","db_host"), # host name
                port = int(config.get("DB","db_port")), # db port
                user = config.get("DB","db_user"), # user name
                password = config.get("DB","db_password"), # password
                db = config.get("DB","db_name"), # db name
                charset = config.get("DB","db_charset")
            )                
            # DB접속
            print ("["+str(datetime.now())+"] Bypass Log : DB Connection Start")
            cursor = conn.cursor()
            # mgreader_log 테이블에 device_id와 mg_data insert
            sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);" 
            val = (device_id, "__PASS_"+sdata)
            cursor.execute(sql, val)
            conn.commit()
            conn.close()
            print ("["+str(datetime.now())+"] Bypass Log : DB Connection End") 
            # 다른톤의 문이 열렸습니다. 음성 재생
            os.system("mpg123 -q " + "/root/door_open_limit.mp3")
            bypass = False
            
            # BYPASS 완료 후 잔존데이터 제거 - 2022.07.08
            while True:
                try:
                    results = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, timeout=5)
                    data += results
                    datalist.append(results)
                    swiped = True

                except usb.core.USBError as e:
                    if e.args[1] == 'Operation timed out' and swiped:
                        break # timeout and swiped means we are done
            
            # 카드읽기 성공하였으므로 프로그램 종료처리 - 2022.07.08.
            print("["+str(datetime.now())+"] Door Open OK! Program Killed!!")        
            break            
            
            
        except pymysql.err.InternalError as e:
            code, msg = e.args
        continue
    else:
        # 문이 열렸습니다. 음성 재생
        os.system("mpg123 -q " + "/root/door_open.mp3")

    #정상 인증인 경우 DB에 기록
    try:
        # 마그네틱 카드 정보를 db에 insert하기 위한 connection 정보
        conn = pymysql.connect(
            host = config.get("DB","db_host"), # host name
            port = int(config.get("DB","db_port")), # db port
            user = config.get("DB","db_user"), # user name
            password = config.get("DB","db_password"), # password
            db = config.get("DB","db_name"), # db name
            charset = config.get("DB","db_charset")
        )
        # DB접속
        print ("["+str(datetime.now())+"] Auth Log : DB Connection Start")
        cursor = conn.cursor()
        # mgreader_log 테이블에 device_id와 mg_data insert
        sql = "insert into mgreader_log(device_id,mg_data) values(%s, %s);" 
        val = (device_id, sdata)
        cursor.execute(sql, val) # db insert
        conn.commit() # db commit
        conn.close() # db 연결 종료
        print ("["+str(datetime.now())+"] Auth Log : DB Connection End") 

        # 정상인증 완료 후 잔존데이터 제거 - 2022.07.08
        while True:
            try:
                results = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, timeout=5)
                data += results
                datalist.append(results)
                swiped = True

            except usb.core.USBError as e:
                if e.args[1] == 'Operation timed out' and swiped:
                    break # timeout and swiped means we are done
        
        # 카드읽기 성공하였으므로 프로그램 종료처리 - 2022.07.08.
        print("["+str(datetime.now())+"] Door Open OK! Program Killed!!")        
        break
    except pymysql.err.InternalError as e:
            code, msg = e.args
