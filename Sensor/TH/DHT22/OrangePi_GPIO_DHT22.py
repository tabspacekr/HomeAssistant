from pyA20.gpio import gpio
from pyA20.gpio import port

import dht
import time
import datetime
import requests

# initialize GPIO
PIN2 = port.PG7
#PIN2 = port.PA6
gpio.init()

# read data using pin
instance = dht.DHT(pin=PIN2)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: {0:0.1f} C".format(result.temperature))
        print("Humidity: {0:0.1f} %".format(result.humidity))
    #print(str(datetime.datetime.now()))
    #print("T: {0:0.01f} C".format(result.temperature))
    #print("H: {0:0.01f} %".format(result.humidity))
        #print("waiting..")
        headers = {
          'Content-Type': 'application/json',
        }
        data = '{"temp": '+str(result.temperature)+', "humi": '+str(result.humidity)+'}'
        response = requests.post('https://your.homeassistant.site/api/webhook/th-webhook', headers=headers, data=data)
    time.sleep(10)
