#debian11 install

apt update && apt upgrade -y && apt autoremove -y

apt-get install -y software-properties-common apparmor-utils apt-transport-https ca-certificates curl dbus jq network-manager

curl -fsSL get.docker.com | sh

wget https://github.com/home-assistant/os-agent/releases/download/1.2.2/os-agent_1.2.2_linux_x86_64.deb

sudo dpkg -i os-agent_1.2.2_linux_x86_64.deb

apt install udisks2

apt --fix-broken install

wget https://github.com/home-assistant/supervised-installer/releases/latest/download/homeassistant-supervised.deb

dpkg -i homeassistant-supervised.deb

ufw disable

#change timezone
timedatectl set-timezone Asia/Seoul

#connect http://ipaddress:8123
