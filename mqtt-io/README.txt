orange pi mqtt_io를 통한 home assistant integration

orange pi gpio pip패키지(OrangePi.GPIO)가 debian 11(bullseye)에 기본내장된 python 3.9에서는 동작하지 않고, debian 10(buster) python 3.7에서만 pip패키지가 설치됨.
따라서, 가상환경으로 python3.7로 동작하도록 수정하거나, debian 10(buster)로 다운그래이드하여 python3.7환경을 맞춰주어야 함.

# if you don't do GPIO.cleanup() you don't free the pin and you will get wrnings
# Use this example, it is ctrl+c friendly
# https://github.com/Jeremie-C/OrangePi.GPIO/blob/master/example/blink_led.py

apt install python3-dev
apt install python3-setuptools
apt install python3-pip
pip3 install wheel
pip3 install OrangePi.GPIO
pip3 install mqtt-io
vi config.yml

==== config.yml ====
mqtt:
  host: mqtt.hostname.com
  port: 1883
  user: mqtt
  password: mqttpassword
  topic_prefix: gpio
  ha_discovery:
   enabled: yes
   name: mqttname

# GPIO
gpio_modules:
  # Use the Orange Pi built-in GPIO
  - name: pi_gpio 
    module: orangepi
    board: zero
    mode: board

digital_inputs:
  # Pin 0 is an input connected to a doorbell button
  - name: door_sensor
    module: pi_gpio
    pin: 7 
    pulldown: True
    ha_discovery:
      name: mqtt_door_sensor_test
      device_class: door

digital_outputs:
  # Pin 0 is an input connected to a doorbell button
  - name: door_sensor
    module: pi_gpio
    pin: 1
    ha_discovery:
      name: mqtt_switch_test
      device_class: switch
====================

python3 -m mqtt_io config.yml


====

digital_inputs:
  - name: gpio_motion_sensor
    module: pi_gpio
    pin: 7 
    pulldown: True
    # 모션센서 활용
    #inverted: True
    ha_discovery:
      name: gpio_motion_sensor
      device_class: motion 

====

pyotp 기반의 네트워크통신단절시에도 동작하는 모듈 
