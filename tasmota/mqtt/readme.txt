#sonoff zigbee bridge tasmota f/w 시의 zigbee2tasmota 처리 방법
- https://zigbee.blakadder.com/Sonoff_ZBBridge.html
- https://github.com/arendst/Tasmota/raw/development/tools/fw_SonoffZigbeeBridge_ezsp/ncp-uart-sw_6.7.8_115200.ota

# zigbee 채널 변경
- zbconfig {"Channel":25}

# zigbee device 삭제
- zbforget 0xB427

zbname 0x662e, door_sensor
- https://www.zigbee2mqtt.io/devices/MCCGQ12LM.html
- Exposes	contact, battery, voltage, linkquality

#도어센서 닫힘
10:40:27.213 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x662E":{"Device":"0x662E","Name":" door_sensor","0500<00":"200000010000","ZoneStatusChange":32,"ZoneStatusChangeZone":1,"Contact":0,"Endpoint":1,"LinkQuality":157}}}
#도어센서 열림
10:40:32.750 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x662E":{"Device":"0x662E","Name":" door_sensor","0500<00":"210000010000","ZoneStatusChange":33,"ZoneStatusChangeZone":1,"Contact":1,"Endpoint":1,"LinkQuality":157}}}

zbname 0x057B, motion_sensor
- https://www.zigbee2mqtt.io/devices/RTCGQ12LM.html
- Exposes	occupancy, battery, occupancy_timeout, linkquality

#모션반응
10:41:26.618 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":1,"Endpoint":1,"LinkQuality":194}}}
#모션미반응
10:43:22.350 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":0,"Endpoint":1,"LinkQuality":204}}}

zbname 0x5E54, scene_button
- https://www.zigbee2mqtt.io/devices/WXKG13LM.html
- Exposes	battery, voltage, action, linkquality

#원클릭
10:44:33.301 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x5E54":{"Device":"0x5E54","Name":" scene_button","0006!02":"","Power":2,"Endpoint":1,"LinkQuality":128}}}
#더블클릭
10:44:36.772 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x5E54":{"Device":"0x5E54","Name":" scene_button","0006!00":"","Power":0,"Endpoint":1,"LinkQuality":92}}}

zbname 0x221C,	tuya 모션센서 RH3040
- https://www.zigbee2mqtt.io/devices/RH3040.html
- Exposes	battery, occupancy, battery_low, tamper, linkquality

#모션반응
02:18:52.709 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x221C":{"Device":"0x221C","0500<00":"010000010000","ZoneStatusChange":1,"ZoneStatusChangeZone":1,"Occupancy":1,"Endpoint":1,"LinkQuality":173}}}
#모션미반응
02:17:12.023 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x221C":{"Device":"0x221C","0500<00":"000000010000","ZoneStatusChange":0,"ZoneStatusChangeZone":1,"Occupancy":0,"Endpoint":1,"LinkQuality":168}}}

zbname 0xCBA4, tuya 도어센서 RH3001
- https://www.zigbee2mqtt.io/devices/TS0203.html
- Exposes	contact, battery_low, tamper, battery, linkquality

#닫힘
02:21:54.799 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0xCBA4":{"Device":"0xCBA4","Name":" Tuya_Door_Sensor","0500<00":"000000010000","ZoneStatusChange":0,"ZoneStatusChangeZone":1,"Contact":0,"Endpoint":1,"LinkQuality":141}}}

#열림
02:22:55.736 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0xCBA4":{"Device":"0xCBA4","Name":" Tuya_Door_Sensor","0500<00":"010000010000","ZoneStatusChange":1,"ZoneStatusChangeZone":1,"Contact":1,"Endpoint":1,"LinkQuality":139}}}

#MQTT 개별 Publish
- https://tasmota.github.io/docs/Zigbee/#sending-sensor-values-to-separated-mqtt-topics
Rule<x>
  on zbreceived#<zigbee_id>#<zigbee_sensorname> do publish home/zigbee/<zigbee_name>/<sensorname> %value% endon
Rule<x> 1

#예제(도어센서 0x662E)
Rule1 on ZbReceived#0x662E#Contact do publish homeassistant/binary_sensor/door_sensor/contact %value% endon
Rule1 1

#in configuration.yaml
binary_sensor: !include binary_sensor.yaml

#in binary_sensor.yaml
- platform: mqtt
  name: "mqtt_door_sensor"
  state_topic: "tele/SonoffZB/SENSOR"
  value_template: "{{ value_json.ZbReceived['0x662E'].Contact }}"
  device_class: door
  payload_on: 1
  payload_off: 0
- platform: mqtt
  name: "mqtt_motion_sensor"
  state_topic: "tele/SonoffZB/SENSOR"
  value_template: "{{ value_json.ZbReceived['0x057B'].Occupancy }}"
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
  value_template: "{{ value_json.ZbReceived['0x5E54'].Power }}"
  



  
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
