# tasmota + DS3231 작업가이드

1. https://gitpod.io/#https://github.com/benzino77/tasmocompiler 에서 firmware 생성 (github id필요 및 팝업차단 해제 필요)

2. 아래절차진행
2-1. Tasmota source code [DOWNLOAD SOURCE] 클릭 후 [NEXT]
2-2. WiFi 설정 NEXT
2-3. Which features should be included in final binary firmware? 에서 [Home Assistant] 추가 체크
2-4. Custom parameters 에서 아래 내용으로 추가

#define PROJECT                "Timer" 
#define DEVICE_NAME          "Timer" 
#define FRIENDLY_NAME          "Timer" 
#define MQTT_USE               true 
#define MQTT_HOST               "input.your.mqtt.address" 
#define MQTT_PORT               1883
#define MQTT_USER            "input_mqtt_id" 
#define MQTT_PASS            "input_mqtt_password" 
#define WEB_PASSWORD           "input_web_admin_password" 
#define NTP_SERVER1            "pool.ntp.org" 
#define APP_TIMEZONE           9
#define USER_TEMPLATE "{\"NAME\":\"Sonoff RE5V1C\",\"GPIO\":[17,255,255,255,255,255,0,0,21,56,0,0,0],\"FLAG\":0,\"BASE\":18}" 
#define MODULE USER_MODULE
#define USE_I2C
#ifndef USE_DS3231
#define USE_DS3231          // DS3231 external RTC (+1k2 code)
#define USE_RTC_ADDR  0x68                   // Default I2C address 0x68
#endif

2-5. Select version v11.0.0, English/English 로 체크 후 [COMPILE] 버튼 클릭
잠시 가디라면 firmware.bin 파일 생성됨.

3. 참고
- sonoffre5v1c 결선도 https://templates.blakadder.com/sonoff_RE5V1C.html
- DS3231 결선방식 https://tasmota.github.io/docs/DS3231/
- tasmotizer https://github.com/tasmota/tasmotizer/releases/tag/v.1.2 
