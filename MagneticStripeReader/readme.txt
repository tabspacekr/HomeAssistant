신용/체크카드/삼성페이 기반 마그네틱 출입관리기
- 무인매장에 불특정 다수를 상대로한 출입통제
- 누구나 가지고 있는 신용/체크카드의 마그네틱 정보를 통한 출입인증 방식

데드볼트락 or EM락 + 퇴실(EXIT)버튼 + OrangePi Zero LTS + MSR100 + GPIO Relay 로 출입관리기 구현

To Do List
- 향후 근태관리 등으로 활용이 가능하도록 NFC(RFID)등 기능 보완 예정
- 지정된 온습도에 따라 제어가 가능한 자동제어 기능 보강
   -> 화재시에 출입문 강제개방을 위함
   -> mqtt-io로 gpio pin에 DHT22 센서추가하여 구현
- evdev python module로 전환
- mqtt.io가 mqtt broker와 단절된경우에 process kill하여 재실행하도록 정교화

적용 완료 사항
- 딜레이 이슈 보강
  - 유선구성으로, 무선환경 배제(sonoff relay 미사용)
- 리눅스 로그 정리 및 자동 재부팅 기능 적용
  - crontab 설정에서 reboot -f, 스케쥴링 재부팅
- GPIO PIN을 통한 외부 Sonoff RE5V1C 드라이락 릴레이 없이 제어 가능하도록 처리
- 스피커를 통한 음성안내가 외부설치환경에서는 잘들리지않아 상태LED 4개를 통한 안내보강
- 전등 및 climate domain에 사용이 가능한 타이머 기능 보강 (input_datetime 선언)
- 기타 기능 보완
  - 인터넷 또는 WIFI가 단절되더라도 exit버튼으로 퇴실가능하도록 하드웨어적으로 설계 변경
  - orange pi자체 gpio제어 처리


설치 필요 패키지
sudo apt install python3
sudo apt install python3-pip
sudo apt install mpg123
sudo pip3 install usb
sudo pip3 install pyusb
sudo pip3 install pymysql
sudo pip3 install requests

구 버전 적용 사항 (신규버전에서는 지원중단)
- SONOFF InchingRelay 사용
- SONOFF GPIO Port(ERX, ETX 활용)를 통한 Tasmota 제어(Magnetic Door Sensor, Exit Button 기능 구현) 
- 별도의 USB형 외부 사운드카드를 적용하여 출입문 열릴 시에 음성으로 안내
-- door_open.mp3 : '문이 열렸습니다' (카드가 정상 인식된 경우)
-- door_open_limit.mp3 : '문이 열렸습니다' (카드인식 3회 연속 오류이나, 매장출입을 진행하기 위함. 목소리톤만 다르게 멘트)
-- door_close.mp3 : '경비중입니다. 문이 열리지 않습니다' (HA에서 출입제한모드로 설정한 경우)
-- error.mp3 : '카드 인식에 실패했습니다. 다시 시도해주세요' (카드 인식이 실패한 경우)


작업완료 후 시간을 정상적으로 한국표준시로 적용하기 위해 linux console에서 아래 명령어 입력
timedatectl set-timezone Asia/Seoul

참고사이트 
- https://chloro.tistory.com/107 백그라운드프로세스 nohup
- https://hue9010.github.io/etc/process_kill/ 리눅스에서 kill, pkill를 통해 특정 프로세스 종료시키기
- https://velog.io/@seunghoking/python-requests%EB%A1%9C-%EC%97%AC%EB%9F%AC%EB%B2%88-http%EC%9A%94%EC%B2%AD%ED%95%A0-%EB%95%8Crequests.exceptions.ConnectionError-HTTPConnectionPool-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95 python requests로 여러번 http요청할 때requests.exceptions.ConnectionError: HTTPConnectionPool 해결 방법
- https://yoonbh2714.blogspot.com/2017/01/ubuntu-unexpected-operator_97.html Ubuntu unexpected operator 쉘스크립트 에러
- http://daplus.net/unix-ps-%EA%B2%B0%EA%B3%BC%EC%97%90-grep%EC%9D%B4-%EB%82%98%ED%83%80%EB%82%98%EC%A7%80-%EC%95%8A%EB%8F%84%EB%A1%9D%ED%95%98%EB%A0%A4%EB%A9%B4-%EC%96%B4%EB%96%BB%EA%B2%8C%ED%95%B4%EC%95%BC/ [unix] ps 결과에 ‘grep’이 나타나지 않도록하려면 어떻게해야합니까?
- https://blog.naver.com/jeong2091/221970687773 리눅스(Linux) 프로세스 자동 재시작 쉘 스크립트 작성하는법!!
- https://blog.daum.net/sualchi/13721064 SQL 접속시 접속정보 별도 보관해서 사용하기(python)
