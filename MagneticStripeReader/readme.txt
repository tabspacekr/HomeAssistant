무인매장 출입관리기 개발

데드볼트 + 퇴실(EXIT)버튼 + SONOFF InchingRelay + OrangePi Zero LTS + MSR100 으로 출입관리기 구현
SONOFF GPIO Port(ERX, ETX 활용)를 통한 Tasmota 제어(Magnetic Door Sensor, Exit Button 기능 구현) 

향후 NFC(RFID)등 기능 보완 예정, 기타 기능 보완 예정 (인터넷 또는 WIFI가 단절되더라도 exit버튼으로 퇴실가능하도록)

설치 필요 패키지
sudo apt install python3
sudo apt install python3-pip
sudo pip3 install usb
sudo pip3 install pyusb
sudo pip3 install pymysql
sudo pip3 install requests

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
