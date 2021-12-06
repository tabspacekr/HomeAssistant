#sonoff zigbee bridge tasmota f/w 시의 zigbee2tasmota 처리 방법
- https://zigbee.blakadder.com/Sonoff_ZBBridge.html
- https://github.com/arendst/Tasmota/raw/development/tools/fw_SonoffZigbeeBridge_ezsp/ncp-uart-sw_6.7.8_115200.ota

# zigbee 채널 변경
- zbconfig {"Channel":25}

# zigbee 디바이스 이름 변경
- zbname 0x1234,Sensor_Name

# zigbee device 삭제
- zbforget 0xB427

# 손쉬운 mqtt사용을 위한 ZbReceived 노출순서 변경
02:43:18.045 CMD: setoption83 1
02:43:18.049 MQT: stat/SonoffZB/RESULT = {"SetOption83":"ON"}

#적용 전
02:37:25.203 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0xCBA4":{"Device":"0xCBA4","Name":"Tuya_Door_Sensor","0500<00":"010000010000","ZoneStatusChange":1,"ZoneStatusChangeZone":1,"Contact":1,"Endpoint":1,"LinkQuality":144}}}

#적용 후
02:45:47.498 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"xiaomi_motion_sensor":{"Device":"0x057B","Name":"xiaomi_motion_sensor","Occupancy":0,"Endpoint":1,"LinkQuality":178}}}


*** 샤오미 도어센서 ***
zbname 0x662e,door_sensor
- https://www.zigbee2mqtt.io/devices/MCCGQ12LM.html
- Exposes	contact, battery, voltage, linkquality

#도어센서 닫힘
10:40:27.213 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x662E":{"Device":"0x662E","Name":" door_sensor","0500<00":"200000010000","ZoneStatusChange":32,"ZoneStatusChangeZone":1,"Contact":0,"Endpoint":1,"LinkQuality":157}}}
#도어센서 열림
10:40:32.750 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x662E":{"Device":"0x662E","Name":" door_sensor","0500<00":"210000010000","ZoneStatusChange":33,"ZoneStatusChangeZone":1,"Contact":1,"Endpoint":1,"LinkQuality":157}}}

*** 샤오미 모션센서 ***
zbname 0x057B,motion_sensor
- https://www.zigbee2mqtt.io/devices/RTCGQ12LM.html
- Exposes	occupancy, battery, occupancy_timeout, linkquality

#모션반응
10:41:26.618 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":1,"Endpoint":1,"LinkQuality":194}}}
#모션미반응
10:43:22.350 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":0,"Endpoint":1,"LinkQuality":204}}}

*** 샤오미 씬스위치 ***
zbname 0x5E54, scene_button
- https://www.zigbee2mqtt.io/devices/WXKG13LM.html
- Exposes	battery, voltage, action, linkquality

#원클릭
10:44:33.301 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x5E54":{"Device":"0x5E54","Name":" scene_button","0006!02":"","Power":2,"Endpoint":1,"LinkQuality":128}}}
#더블클릭
10:44:36.772 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x5E54":{"Device":"0x5E54","Name":" scene_button","0006!00":"","Power":0,"Endpoint":1,"LinkQuality":92}}}

*** Tuya 모션센서 ***
zbname 0x221C,	tuya 모션센서 RH3040
- https://www.zigbee2mqtt.io/devices/RH3040.html
- Exposes	battery, occupancy, battery_low, tamper, linkquality

#모션반응
02:18:52.709 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x221C":{"Device":"0x221C","0500<00":"010000010000","ZoneStatusChange":1,"ZoneStatusChangeZone":1,"Occupancy":1,"Endpoint":1,"LinkQuality":173}}}
#모션미반응
02:17:12.023 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x221C":{"Device":"0x221C","0500<00":"000000010000","ZoneStatusChange":0,"ZoneStatusChangeZone":1,"Occupancy":0,"Endpoint":1,"LinkQuality":168}}}

*** Tuya 도어센서 ***
zbname 0xCBA4, tuya 도어센서 RH3001
- https://www.zigbee2mqtt.io/devices/TS0203.html
- Exposes	contact, battery_low, tamper, battery, linkquality

#닫힘
02:21:54.799 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0xCBA4":{"Device":"0xCBA4","Name":" Tuya_Door_Sensor","0500<00":"000000010000","ZoneStatusChange":0,"ZoneStatusChangeZone":1,"Contact":0,"Endpoint":1,"LinkQuality":141}}}

#열림
02:22:55.736 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0xCBA4":{"Device":"0xCBA4","Name":" Tuya_Door_Sensor","0500<00":"010000010000","ZoneStatusChange":1,"ZoneStatusChangeZone":1,"Contact":1,"Endpoint":1,"LinkQuality":139}}}

*** Tuya 온습도센서 ***
zbname 0x2E3A,Tuya_Temp_sensor RH3052
- Exposes	humidity, temperature, battery, linkquality

#메시지 포맷
03:56:31.637 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"Tuya_Temp_sensor":{"Device":"0x2E3A","Name":"Tuya_Temp_sensor","Temperature":25.69,"Humidity":26.17,"Endpoint":1,"LinkQuality":144}}}



************************ EXAMPLE *******************************

#MQTT 개별 Publish
- https://tasmota.github.io/docs/Zigbee/#sending-sensor-values-to-separated-mqtt-topics
Rule<x>
  on zbreceived#<zigbee_id>#<zigbee_sensorname> do publish home/zigbee/<zigbee_name>/<sensorname> %value% endon
Rule<x> 1

#예제(도어센서 0x662E)
Rule1 on ZbReceived#Tuya_Door_Sensor#Contact do publish tabspace/door/001 {"Contact":"%value%"} endon
Rule1 1

Rule2 on ZbReceived#xiaomi_door_sensor#Contact do publish tabspace/door/002 {"Contact":"%value%"} endon
Rule2 1

**test**
Rule1 on ZbReceived#Tuya_Door_Sensor#Contact do publish tabspace/door/001 {"Contact":"%value%"} endon
Rule2 on ZbReceived#xiaomi_door_sensor#Contact do publish tabspace/door/002 {"Contact":"%value%"} endon


Rule1 on ZbReceived#Tuya_Door_Sensor do publish tabspace/door/001 {"Contact":"%value%", "LinkQuality":"%Var2%"} endon


 on ZbReceived#Tuya_Door_Sensor#LinkQuality do publish tabspace/door/001 {} endon

#in configuration.yaml
binary_sensor: !include binary_sensor.yaml

#in binary_sensor.yaml
- platform: mqtt
  name: "mqtt_door_sensor"
  state_topic: "tele/SonoffZB/SENSOR"
  value_template: "{{ value_json.ZbReceived['xiaomi_door_sensor'].Contact }}"
  device_class: door
  payload_on: 1
  payload_off: 0
- platform: mqtt
  name: "mqtt_motion_sensor"
  state_topic: "tele/SonoffZB/SENSOR"
  value_template: "{{ value_json.ZbReceived['xiaomi_motion_sensor'].Occupancy }}"
  device_class: motion
  payload_on: 1
  payload_off: 0

- platform: mqtt
  name: "tuya_mqtt_door_sensor"
  state_topic: "tele/SonoffZB/SENSOR"
  value_template: "{{ value_json.ZbReceived['Tuya_Door_Sensor'].Contact }}"
  device_class: door
  payload_on: 1
  payload_off: 0
- platform: mqtt
  name: "tuya_mqtt_motion_sensor"
  state_topic: "tele/SonoffZB/SENSOR"
  value_template: "{{ value_json.ZbReceived['Tuya_Motion_Sensor'].Occupancy }}"
  device_class: motion
  payload_on: 1
  payload_off: 0
 
  
# binary_sensor device_class list
- https://www.home-assistant.io/integrations/binary_sensor/

#in configuration.yaml
sensor: !include sensor.yaml

#in sensor.yaml  
- platform: mqtt
  name: "mqtt_button"
  state_topic: "tele/SonoffZB/SENSOR"
  value_template: "{{ value_json.ZbReceived['xiaomi_button_switch'].Power }}"
  
- platform: mqtt
  name: "tuya_mqtt_temperature"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: temperature
  unit_of_measurement: "°C"
  value_template: "{{ value_json.ZbReceived['Tuya_Temp_sensor'].Temperature }}"

- platform: mqtt
  name: "tuya_mqtt_humidity"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: humidity
  unit_of_measurement: "%"
  value_template: "{{ value_json.ZbReceived['Tuya_Temp_sensor'].Humidity }}"

#lqi
- platform: mqtt
  name: "Tuya_Door_Sensor_LQI"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: signal_strength
  unit_of_measurement: "LQI"
  value_template: "{{ value_json.ZbReceived['Tuya_Door_Sensor'].LinkQuality }}"
- platform: mqtt
  name: "Tuya_Motion_Sensor_LQI"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: signal_strength
  unit_of_measurement: "LQI"
  value_template: "{{ value_json.ZbReceived['Tuya_Motion_Sensor'].LinkQuality }}"
- platform: mqtt
  name: "Tuya_Temp_sensor_LQI"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: signal_strength
  unit_of_measurement: "LQI"
  value_template: "{{ value_json.ZbReceived['Tuya_Temp_sensor'].LinkQuality }}"
- platform: mqtt
  name: "xiaomi_button_switch_LQI"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: signal_strength
  unit_of_measurement: "LQI"
  value_template: "{{ value_json.ZbReceived['xiaomi_button_switch'].LinkQuality }}"
- platform: mqtt
  name: "xiaomi_door_sensor_LQI"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: signal_strength
  unit_of_measurement: "LQI"
  value_template: "{{ value_json.ZbReceived['xiaomi_door_sensor'].LinkQuality }}"
- platform: mqtt
  name: "xiaomi_motion_sensor_LQI"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: signal_strength
  unit_of_measurement: "LQI"
  value_template: "{{ value_json.ZbReceived['xiaomi_motion_sensor'].LinkQuality }}"

#battery BatteryPercentage
- platform: mqtt
  name: "Tuya_Door_Sensor_battery"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: battery
  unit_of_measurement: "%"
  value_template: "{{ value_json.ZbReceived['Tuya_Door_Sensor'].BatteryPercentage }}"
- platform: mqtt
  name: "Tuya_Motion_Sensor_battery"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: battery
  unit_of_measurement: "%"
  value_template: "{{ value_json.ZbReceived['Tuya_Motion_Sensor'].BatteryPercentage }}"
- platform: mqtt
  name: "Tuya_Temp_sensor_battery"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: battery
  unit_of_measurement: "%"
  value_template: "{{ value_json.ZbReceived['Tuya_Temp_sensor'].BatteryPercentage }}"
- platform: mqtt
  name: "xiaomi_button_switch_battery"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: battery
  unit_of_measurement: "%"
  value_template: "{{ value_json.ZbReceived['xiaomi_button_switch'].BatteryPercentage }}"
- platform: mqtt
  name: "xiaomi_door_sensor_battery"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: battery
  unit_of_measurement: "%"
  value_template: "{{ value_json.ZbReceived['xiaomi_door_sensor'].BatteryPercentage }}"
- platform: mqtt
  name: "xiaomi_motion_sensor_battery"
  state_topic: "tele/SonoffZB/SENSOR"
  device_class: battery
  unit_of_measurement: "%"
  value_template: "{{ value_json.ZbReceived['xiaomi_motion_sensor'].BatteryPercentage }}"



  
  value_template: |-
    {% if {{ value_json.ZbReceived['0x5E54'].Power }} == 2 %}
      {{ value | round(2) }}
    {% else %}
      {{ value | round(2) * 0.9 + states(entity_id) * 0.1 }}
    {% endif %}

# sensor device_class list
- https://www.home-assistant.io/integrations/sensor.mqtt/

# tip
- json parser online : http://json.parser.online.fr/

Sonoff ZbBridge
Tasmota-SonoffZB


🕗01m
Device 	 	
🕗02m
Device 0x662E		
🕗03m
