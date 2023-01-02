use asterisk sip voip protocol 
freepbx
- https://wiki.freepbx.org/display/FOP/Version+14.0+Installation

https://wiki.freepbx.org/display/FOP/Installing+FreePBX+14+on+Ubuntu+18.04

#에러 관련
Exception SQLSTATE[HY000] [2002] Connection refused::SQLSTATE[HY000] [2002] Connection refused

이런식으로 웹페이지가 표시되며 접속이 안되는경우
cd /var/log/asterisk
밑에 fail2ban, full 로그파일 삭제

vi /etc/fail2ban/fail2ban.conf
loglevel을 4debug를 1로 변경

이후 systemctl restart mariadb 하여 db서비스 재시작

#원론적인 에러 처리 방법
5060포트가 공개되어, 무차별대입접속이 들어오는 문제.
SIP통신포트인 5060을 비정규포트로 변경 
- https://techoverflow.net/2021/06/24/how-to-change-sip-port-in-freepbx/

부득이하게 5060포트를 공개해야하는경우, firewalld on후 해외 ip를 차단하기위해 kr.zone을 whitelist로 
