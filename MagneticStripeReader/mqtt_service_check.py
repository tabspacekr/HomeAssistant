#!/usr/bin/env python
# mqtt-io가 인터넷접속이 불안정하면 프로그램은 실행되어 있으나 mqtt통신을 하지 못하고 복구되지 않는 이슈가 있어, 해당 ha entity를 모니터링하여 unavailable상태가 되면 프로그램 재시동처리
# mqtt-io 프로세스가 강제로 kill 된 경우, unavailable이 되지 않으므로 주의 필요
# File name : mqtt_service_check.py
# 2022.08.09. ceo@tabspace.kr
# crontab에 아래 추가
## @reboot python3 /root/mqtt_service_check.py
## * * * * * python3 /root/mqtt_service_check.py
## * * * * * sleep 30; python3 /root/mqtt_service_check.py

import requests
import os 
import sys
import time
from datetime import datetime
import json
from requests import get
import configparser
from time import sleep          # this lets us have a time delay

# 환경 설정 파일 호출
config = configparser.ConfigParser()
config.read('mg.ini')

# HA 사이트와 엔티티를 환경설정파일에서 불러옴
ha_site = config.get("HA","ha_site")
device_id = config.get("DB","device_id")

ha_url = "https://"+ha_site+"/api/states/switch."+device_id+"_lock"
ha_token = config.get("HA","ha_token")
ha_headers = {
    "Authorization": "Bearer "+ha_token,
    "content-type": "application/json",
    }

try: # Rest API로 HA에 상태 호출
    ha_response = get(ha_url, headers=ha_headers)
    ha_entity_state = json.loads(ha_response.text)["state"]
    # ha_entity_state : unavailable (접속불가)
    print("["+str(datetime.now())+"] Current HA state = ["+ha_entity_state+"]")
except: # Rest API가 미동작이면 네트워크 연결이 안되었다는 뜻
    print("Error! Check HA Connection!")
    
if ha_entity_state == "unavailable": # 사용불가 상태로 된 경우, mqtt-io 서비스 재시작해줌
    print("HA Entity Unavailable")
    os.system("pkill -9 -f 'python3 -m mqtt_io /root/config.yml'")
    print("["+str(datetime.now())+"] MQTT-IO Service Restart!")
else: # on 또는 off 상태는 정상상태임. 프로그램 종료.
    print("["+str(datetime.now())+"] HA Work!!")
