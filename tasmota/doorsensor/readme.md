Sonoff basic R2 활용 도어센서모니터링

사전정보
<pre>
gpio3 = rx
gpio1 = tx
</pre>

접점제어 방식으로, 도어센서2개를 사용할 수 없을까 하여 테스트해보았으나, 테스트결과 tx쪽은 활용할수없는것으로 보임.

절차
<pre>
1. sonoff basic r2 wifi relay에 4pin 부분 핀헤더 납땜하여 tasmota 펌업
2. 전원 인가 후 wifi연결 및 IP주소 식별
3. IP주소로 웹페이지 들어간 후, 설정 - 모듈설정 - gpio3를 switch 2로 설정 (자동재부팅)
4. 재부팅 후 설정페이지에서 mqtt설정
5. tasmota 콘솔에서 다음 커맨드 입력
   - Switchtopic test_room
6. tasmota 콘솔에서 다음 커맨드 입력
   - SwitchMode2 1
7. tasmota 콘솔에서 다음 커맨드 입력
   - SwitchRetain on
8. ha에서 configuration.yaml 설정
binary_sensor:
  - platform: mqtt
    name: "contact sensor test"
    state_topic: "cmnd/test_room/POWER2"
    payload_on: "ON"
    payload_off: "OFF"
    device_class: door
</pre>

참고

<img src="https://raw.githubusercontent.com/tabspacekr/HomeAssistant/main/tasmota/doorsensor/sonoff_basic_r2_1.jpg">
<img src="https://raw.githubusercontent.com/tabspacekr/HomeAssistant/main/tasmota/doorsensor/sonoff_basic_r2_2.jpg">
<img src="https://raw.githubusercontent.com/tabspacekr/HomeAssistant/main/tasmota/doorsensor/sonoffbasic_sensor_ha.png">
