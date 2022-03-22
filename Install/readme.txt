#debian11 bullseye install

apt update && apt upgrade -y && apt autoremove -y

#요구 패키지 설치
apt-get install -y software-properties-common apparmor-utils apt-transport-https ca-certificates curl dbus jq network-manager

#docker 설치
curl -fsSL get.docker.com | sh

#home assistant release 사이트에서 최신 버전을 확인
wget https://github.com/home-assistant/os-agent/releases/download/1.2.2/os-agent_1.2.2_linux_x86_64.deb
sudo dpkg -i os-agent_1.2.2_linux_x86_64.deb

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
