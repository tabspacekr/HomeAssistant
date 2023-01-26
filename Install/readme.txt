#debian11 bullseye home assistant supervisor install

apt update && apt upgrade -y && apt autoremove -y

#요구 패키지 설치
apt-get install -y software-properties-common apparmor-utils apt-transport-https ca-certificates curl dbus jq network-manager

#docker 설치
curl -fsSL get.docker.com | sh

#home assistant release 사이트에서 최신 버전을 확인
wget https://github.com/home-assistant/os-agent/releases/download/1.4.1/os-agent_1.4.1_linux_x86_64.deb
sudo dpkg -i os-agent_1.4.1_linux_x86_64.deb 

apt install udisks2

apt --fix-broken install

#supervisor 다운로드, docker compose하여 자동으로 ha인스톨
wget https://github.com/home-assistant/supervised-installer/releases/latest/download/homeassistant-supervised.deb
dpkg -i homeassistant-supervised.deb

#방화벽 해제
ufw disable

#change timezone
timedatectl set-timezone Asia/Seoul

#connect http://ipaddress:8123


===============================================

강제종료 등의 이유로 homeassistant supervisor의 docker실행이 불가한경우
/usr/share/hassio/ 경로를 유지한 상태로 docker의 컨테이너만 삭제 후, 위 설치 절차 진행

docker stop 으로 home assistant와 유관된 모든 docker service stop
이후
docker system prune 
명령어를 통해 초기화

addon은 재설치를 해주어야하지만, 나머지 정보는 유지가 가능함.

Ref: https://www.lainyzine.com/ko/article/docker-prune-usage-remove-unused-docker-objects/
