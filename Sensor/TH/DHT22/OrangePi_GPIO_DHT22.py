# HA의 webhook api를 활용한 dht22 온도/습도 정보 전송
from pyA20.gpio import gpio
from pyA20.gpio import port

import dht
import time
import datetime
import requests

# initialize GPIO
# Orange Pi BCM Numbering : https://opi-gpio.readthedocs.io/en/latest/api-documentation.html
PIN2 = port.PG7
#PIN2 = port.PA6
gpio.init()

# read data using pin
instance = dht.DHT(pin=PIN2)

while True:
    result = instance.read()
    # value가 유효할때만 데이터 출력 및 webhook으로 전송
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: {0:0.1f} C".format(result.temperature))
        print("Humidity: {0:0.1f} %".format(result.humidity))
        # webhook으로 데이터 전송
        headers = {
          'Content-Type': 'application/json',
        }
        data = '{"temp": '+str(result.temperature)+', "humi": '+str(result.humidity)+'}'
        response = requests.post('https://your.homeassistant.site/api/webhook/th-webhook', headers=headers, data=data)
    time.sleep(10)
