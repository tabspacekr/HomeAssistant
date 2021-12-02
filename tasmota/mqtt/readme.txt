zbconfig {"Channel":25}

zbforget 0xB427

zbname 0x662e, door_sensor
- https://www.zigbee2mqtt.io/devices/MCCGQ12LM.html
- Exposes	contact, battery, voltage, linkquality

zbname 0x057B, motion_sensor
- https://www.zigbee2mqtt.io/devices/RTCGQ12LM.html
- Exposes	occupancy, battery, occupancy_timeout, linkquality

zbname 0x5E54, scene_button
- https://www.zigbee2mqtt.io/devices/WXKG13LM.html
- Exposes	battery, voltage, action, linkquality

10:30:24.413 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":1,"Endpoint":1,"LinkQuality":105}}}
10:31:54.095 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":0}}}
10:33:26.136 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":0,"Endpoint":1,"LinkQuality":94}}}
10:34:24.544 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":1,"Endpoint":1,"LinkQuality":94}}}
10:35:15.417 MQT: tele/SonoffZB/STATE = {"Time":"2021-12-02T10:35:15","Uptime":"0T01:55:09","UptimeSec":6909,"Vcc":3.438,"Heap":27,"SleepMode":"Dynamic","Sleep":0,"LoadAvg":999,"MqttCount":1,"Wifi":{"AP":1,"SSId":"BarunsonStay","BSSId":"EC:08:6B:DD:AE:96","Channel":1,"Mode":"11n","RSSI":100,"Signal":-41,"LinkCount":1,"Downtime":"0T00:00:03"}}
10:35:54.195 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":0}}}
10:36:58.537 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":0,"Endpoint":1,"LinkQuality":84}}}
10:38:32.638 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":1,"Endpoint":1,"LinkQuality":92}}}

08:10:52.106 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x5E54":{"Device":"0x5E54","Name":" scene_button","0006!02":"","Power":2,"Endpoint":1,"LinkQuality":154}}}

Rule1 on ZbReceived#0x5E54# do publish 

Occupancy
08:12:42.905 MQT: tele/SonoffZB/SENSOR = {"ZbReceived":{"0x057B":{"Device":"0x057B","Name":" motion_sensor","Occupancy":1,"Endpoint":1,"LinkQuality":165}}}


binary_sensor

- platform: mqtt
  name: "mqtt_door_sensor"
  state_topic: "tele/sonoff-z2t/SENSOR"
  value_template: "{{ value_json.ZigbeeReceived['0x2E8F'].Power }}"
  device_class: window
  payload_on: true
  payload_off: false




Sonoff ZbBridge
Tasmota-SonoffZB


🕗01m
Device 	 	
🕗02m
Device 0x662E		
🕗03m
