Tuya 기반의 국내유통 IoT디바이스(헤이홈 등) IR remote 제품은 tasmota에서 YTF로 설정

tasmota로 flashing 한 후 module을 YTF IR(62)로 변경 후 mqtt로 제어 (mqtt broker에서 설정한 정보 입력)
- firmware upgrade 모드 진입시에 gpio0번을 ground로 같이 넣어주어야함
- https://tasmota.github.io/docs/devices/YTF-IR-Bridge/


# HA Integration 관련
tasmota_irhvac.txt을 참고하여, custom_component 추가
- repo : https://github.com/hristo-atanasov/Tasmota-IRHVAC.git

# 이슈사항
- carrier 에어컨은 국내에서만 유통되고 있는것으로 보이며 범용 ir code 미동작
- 학습 기능을 이용해보려 하였으나, 물리적 리모콘에서 버튼을 눌러 발신시에 코드가 랜덤하게 바뀌는 이슈 있음
- GA(google assistant) Integration 시에 power off command가 비정상동작하는 이슈 있음
