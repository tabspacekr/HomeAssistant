#!/usr/bin/env python

# HA MQTT 서비스 INITIAL 상태 체크 및 적용_v2
# 2022.12.26. ceo@tabspace.kr

import requests
import os 
import sys
import time
from datetime import datetime
import json
from requests import get
from time import sleep          # this lets us have a time delay
import configparser

# 환경 설정 파일 호출
config = configparser.ConfigParser()
config.read('mg.ini')

# HA 사이트와 엔티티를 환경설정파일에서 불러옴
ha_site = config.get("HA","ha_site") # xxxxxxxx.tabspace.kr
ha_entity = config.get("HA","ha_entity") # input_select. 뒷부분만 입력, XXXXXXXX_MSRMODE
ha_url = "https://"+ha_site+"/api/states/input_select."+ha_entity 
ha_token = config.get("HA","ha_token")
ha_headers = {
    "Authorization": "Bearer "+ha_token,
    "content-type": "application/json",
    }

try:
    # Rest API로 HA에 mqtt broker state를 받아옴
    ha_response = get(ha_url, headers=ha_headers)
    ha_state = json.loads(ha_response.text)["state"]
    # ha_state : lock, lockdown, unlock
except:
    print("["+str(datetime.now())+"] Current HA State = [ERROR!!]")

# 현재 input_select 상태에 따른 mqtt-io의 initial 및 publish_initial 설정 (사전에 config.yml_initial_open, config.yml_initial_lock으로 선언해야함)
# config.yml_initial_open : _LOCK initial : low 
# config.yml_initial_lock : _LOCK initial : high
if ha_state == "unlock":
    print("["+str(datetime.now())+"] Current HA State = [UNLOCK]")
    os.system("rm /root/config.yml && cp /root/config.yml_initial_open /root/config.yml")
else:
    print("["+str(datetime.now())+"] Current HA State = [LOCK]")
    os.system("rm /root/config.yml && cp /root/config.yml_initial_lock /root/config.yml")
