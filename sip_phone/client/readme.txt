# DO1
gpio포트에 연결된 push button을 누르면 python script가 반응하여 sip client에서 지정된곳으로 call 하는 형태
https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

sip phone agent auto answer (python)
- 통화가 수신이 될때에 자동으로 응답처리
- 오픈소스 sip 프로트콜 linux client 식별

mqtt-io의 gpio mqtt publish 활용

# DO2
android 중고폰을 통한 업사이클링 개념, 또는 전용장비 활용
오픈소스 Linphone을 ( https://www.linphone.org/ ) 커스텀앱 
- android 발신수신 모두 가능
- (linphone의 경우) iphone 발신만가능하고 수신이 불가능
상용 softphone을 통한 iphone지원
- (softphone의 경우) iphone 수/발신 가능. 단, deep sleep mode에 들어가면 수신이 되지 않음. 또한 TCP/TLS프로트콜로 최초 설정하여야함.
