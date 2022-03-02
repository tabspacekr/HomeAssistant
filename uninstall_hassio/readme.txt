root@tabspace:~# systemctl stop hassio-supervisor.service 
root@tabspace:~# systemctl stop hassio-apparmor.service 
root@tabspace:~# docker rmi -f homeassistant/amd64-
homeassistant/amd64-addon-configurator:5.3.3     homeassistant/amd64-hassio-supervisor:2022.01.1
homeassistant/amd64-addon-mariadb:2.4.0          homeassistant/amd64-hassio-supervisor:latest
homeassistant/amd64-addon-mosquitto:6.0.1        
root@tabspace:~# docker rmi -f homeassistant/amd64-hassio-supervisor:latest 
Untagged: homeassistant/amd64-hassio-supervisor:latest
root@tabspace:~# docker rmi -f homeassistant/amd64-addon-configurator:5.3.3 
Untagged: homeassistant/amd64-addon-configurator:5.3.3
Untagged: homeassistant/amd64-addon-configurator@sha256:cc60019fa35cf762d3c2f5b74fc7be3c65ca44a5d24b94e5477feffea174cef4
root@tabspace:~# docker rmi -f homeassistant/amd64-hassio-supervisor:2022.01.1 
Untagged: homeassistant/amd64-hassio-supervisor:2022.01.1
root@tabspace:~# docker rmi -f homeassistant/amd64-addon-m
homeassistant/amd64-addon-mariadb:2.4.0    homeassistant/amd64-addon-mosquitto:6.0.1
root@tabspace:~# docker rmi -f homeassistant/amd64-addon-mariadb:2.4.0 
Untagged: homeassistant/amd64-addon-mariadb:2.4.0
Untagged: homeassistant/amd64-addon-mariadb@sha256:ee7be126452b6bb2cd2fd624e724c9c99c8035f1cff49f19a91dbd47956c58fb
root@tabspace:~# docker rmi -f homeassistant/amd64-addon-mosquitto:6.0.1 
Untagged: homeassistant/amd64-addon-mosquitto:6.0.1
Untagged: homeassistant/amd64-addon-mosquitto@sha256:5eaadc62c70a6d89fb33fd7db32eb3bed0ec722d2c99c030c0548754b3137662


ref: https://community.home-assistant.io/t/ha-supervised-cannot-uninstall-the-docker-script-installation/304250/2
