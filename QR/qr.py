# NOKEY PROJECT QRCODE Reader
# 2022.05.09. ceo@tabspace.kr
# PreRequirements : sudo apt install python3-evdev

import evdev
from evdev import *
import time 
from datetime import datetime

import requests
import json
from requests import get

import socket
print(socket.gethostname())

# /root/hostname.sh 생성
## #!/bin/bash
## HOSTNAME=`echo $(ifconfig eth0|grep ether |awk '{print $2}'|cut -f 4-6 -d':'| tr [:lower:] [:upper:] | sed -e 's/://g')`
## hostnamectl set-hostname ${HOSTNAME}

# 이후에 'crontab -e' 하여 마지막줄에
## @reboot su - root -c /root/hostname.sh
# 를 추가하여준다. (su - root -c 가 없을 시에, 재부팅시에 맥어드레드 뒷 6자리 추출에 실패함)

#qr_site = "TEST01"
qr_site = socket.gethostname()
qr_code = ""

dev =evdev.InputDevice('/dev/input/event1')
#dev =evdev.InputDevice('/dev/input/by-id/usb-0416_5020-if01-event-kbd')
#dev =evdev.InputDevice('/dev/input/by-path/platform-1c1b400.usb-usb-0:1:1.1-event-kbd')
dev.grab()
#print(dev)

# for event in dev.read_loop():
#     if event.type == ecodes.EV_KEY:
#         print(categorize(event))

scancodes = { 
    # Scancode: ASCIICode 
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8', 
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'q', 17: u'w', 18: u'e', 19: u'r', 
    20: u't', 21: u'y', 22: u'u', 23: u'i', 24: u'o', 25: u'p', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL', 
    30: u'a', 31: u's', 32: u'd', 33: u'f', 34: u'g', 35: u'h', 36: u'j', 37: u'k', 38: u'l', 39: u';', 
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'z', 45: u'x', 46: u'c', 47: u'v', 48: u'b', 49: u'n', 
    50: u'm', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 57: u' ', 100: u'RALT' 
} 

capscodes = { 
    0: None, 1: u'ESC', 2: u'!', 3: u'@', 4: u'#', 5: u'$', 6: u'%', 7: u'^', 8: u'&', 9: u'*', 
    10: u'(', 11: u')', 12: u'_', 13: u'+', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R', 
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'{', 27: u'}', 28: u'CRLF', 29: u'LCTRL', 
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u':', 
    40: u'\'', 41: u'~', 42: u'LSHFT', 43: u'|', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N', 
    50: u'M', 51: u'<', 52: u'>', 53: u'?', 54: u'RSHFT', 56: u'LALT', 57: u' ', 100: u'RALT' 
} 
#setup vars 
x = '' 
caps = False 

#grab provides exclusive access to the device 

while True:
    print("["+str(datetime.now())+"] Wait for QR Reader...")
    x = '' # Clear QR Code
    qr_code = '' # Clear QR Code
    #loop, Enter키 감지까지 반복
    for event in dev.read_loop(): 
        if event.type == ecodes.EV_KEY: 
            data = categorize(event) # Save the event temporarily to introspect it 
            if data.scancode == 42: 
                if data.keystate == 1: 
                    caps = True 
                if data.keystate == 0: 
                    caps = False 
            if data.keystate == 1: # Down events only 
                if caps: 
                    key_lookup = u'{}'.format(capscodes.get(data.scancode)) or u'UNKNOWN:[{}]'.format(data.scancode) # Lookup or return UNKNOWN:XX 
                else: 
                    key_lookup = u'{}'.format(scancodes.get(data.scancode)) or u'UNKNOWN:[{}]'.format(data.scancode) # Lookup or return UNKNOWN:XX 
                if (data.scancode != 42) and (data.scancode != 28): 
                    x += key_lookup 
                if(data.scancode == 28): 
                    print (x)   # Print it all out! 
                    qr_code = x
                    # QR리더기로부터 수신한 정보를 api서버로 발송
                    try:
                        print("["+str(datetime.now())+"] Send QR Information Start")
                        qr_url = "https://nokey.tabspace.kr/api/qr.php?qr="+qr_site+qr_code
                        print(qr_url)
                        qr_send = requests.get(qr_url).json
                        print(qr_send)
                        print("["+str(datetime.now())+"] Send QR Information End")
                        break
                    except:
                        print("["+str(datetime.now())+"] Send QR Information Failed!!")
                        break
                    
