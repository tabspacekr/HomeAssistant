# case.1 : ha설치상태는 남겨둔채 docker 자동 시작만 해제하는 경우

서비스 자동시작만 없애는 경우
sudo systemctl mask docker.service
sudo systemctl mask docker.socket

서비스 자동시작만 하는 경우
sudo systemctl unmask docker.service
sudo systemctl unmask docker.socket

========================
# case.2 : ha도커컨테이너 자체를 삭제하는 

HA 서비스 종료 
systemctl stop hassio-supervisor.service 
systemctl stop hassio-apparmor.service 

도커 컨테이너 삭제
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

이후 재설치


root@tabspace:~# docker ps
CONTAINER ID   IMAGE                                                      COMMAND                  CREATED         STATUS         PORTS                                                                                                                          NAMES
6a6473521927   zigbee2mqtt/zigbee2mqtt-amd64:1.23.0-1                     "/init"                  7 minutes ago   Up 7 minutes   0.0.0.0:8485->8485/tcp, :::8485->8485/tcp                                                                                      addon_45df7312_zigbee2mqtt
24911122860b   c9ab7401e439                                               "/init"                  7 minutes ago   Up 7 minutes                                                                                                                                  addon_core_configurator
e684db54698a   ghcr.io/hassio-addons/motioneye/amd64:0.17.0               "/init"                  7 minutes ago   Up 7 minutes                                                                                                                                  addon_a0d7b954_motioneye
d8fbd4d42db0   ghcr.io/hassio-addons/grafana/amd64:7.4.1                  "/init"                  8 minutes ago   Up 8 minutes                                                                                                                                  addon_a0d7b954_grafana
91d30a0e0f04   ghcr.io/hassio-addons/zerotier/amd64:0.12.2                "/init"                  8 minutes ago   Up 8 minutes                                                                                                                                  addon_a0d7b954_zerotier
0f649fd56281   bb7900d6f945                                               "/init"                  8 minutes ago   Up 8 minutes                                                                                                                                  addon_core_mariadb
cf94821b4c09   992f6ea5b83a                                               "/init"                  8 minutes ago   Up 8 minutes   0.0.0.0:1883-1884->1883-1884/tcp, :::1883-1884->1883-1884/tcp, 0.0.0.0:8883-8884->8883-8884/tcp, :::8883-8884->8883-8884/tcp   addon_core_mosquitto
f1f22823bba6   ghcr.io/home-assistant/amd64-hassio-multicast:2021.04.0    "/init"                  8 minutes ago   Up 8 minutes                                                                                                                                  hassio_multicast
94a5e7f0c6db   ghcr.io/home-assistant/amd64-hassio-audio:2021.07.0        "/init"                  8 minutes ago   Up 8 minutes                                                                                                                                  hassio_audio
505dcfa16acc   ghcr.io/home-assistant/amd64-hassio-dns:2021.06.0          "/init"                  8 minutes ago   Up 8 minutes                                                                                                                                  hassio_dns
168856121e65   ghcr.io/home-assistant/amd64-hassio-cli:2021.12.0          "/init /bin/bash -c …"   8 minutes ago   Up 8 minutes                                                                                                                                  hassio_cli
c041d608ec72   ghcr.io/home-assistant/qemux86-64-homeassistant:2022.2.9   "/init"                  9 days ago      Up 8 minutes                                                                                                                                  homeassistant
5f89e2458c24   ghcr.io/home-assistant/amd64-hassio-observer:2021.10.0     "/init"                  3 months ago    Up 8 minutes   0.0.0.0:4357->80/tcp, :::4357->80/tcp                                                                                          hassio_observer
root@tabspace:~# docker rm 5f89e2458c24
Error response from daemon: You cannot remove a running container 5f89e2458c24f9cb99d702ab56858520d16433fceee52d8e88b7f41a78287348. Stop the container before attempting removal or force remove
root@tabspace:~# docker rm -f 5f89e2458c24
5f89e2458c24
root@tabspace:~# docker rm -f c041d608ec72
c041d608ec72
root@tabspace:~# docker rm -f 168856121e65
168856121e65
root@tabspace:~# docker rm -f 505dcfa16acc
505dcfa16acc
root@tabspace:~# docker rm -f 94a5e7f0c6db
94a5e7f0c6db
root@tabspace:~# docker rm -f f1f22823bba6
f1f22823bba6
root@tabspace:~# docker rm -f cf94821b4c09
cf94821b4c09
root@tabspace:~# docker rm -f 0f649fd56281
0f649fd56281
root@tabspace:~# docker rm -f 91d30a0e0f04
91d30a0e0f04
root@tabspace:~# docker rm -f d8fbd4d42db0
d8fbd4d42db0
root@tabspace:~# docker rm -f e684db54698a
e684db54698a
root@tabspace:~# docker rm -f 24911122860b
24911122860b
root@tabspace:~# docker rm -f 6a6473521927
6a6473521927
root@tabspace:~# docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
root@tabspace:~# 


ref: https://www.lainyzine.com/ko/article/docker-rm-removing-docker-containers/
