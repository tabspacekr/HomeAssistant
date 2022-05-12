미세먼지 측정 센서인 SDS011을 라즈베리파이 또는 오렌지파이 등의 SBC에서 인식하여 측정값 표출

1) webhook 호출로 ha에 insert (완료)
2) sql db insert한 자료를 ha에서 읽어와서 표출
3. mqtt-gpio를 통한 mqtt로 publish message하여 ha에서 mqtt를 수동으로 추가 또는 auto discovery하여 자동 추가 하는 형태
