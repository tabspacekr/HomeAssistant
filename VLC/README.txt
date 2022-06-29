ref: https://www.home-assistant.io/integrations/vlc_telnet

Telnet 통신을 통한 VLC media player
- vlc_telnet 플랫폼은 VLC media player를 Telnet 인터페이스로 제어 할 수 있습니다.
- 네트워크에 Telnet 인터페이스가 활성화 되면, HA의 통합모듈을 통해 제어가 가능합니다. 방화벽의 인바운드 포트의 개방이 필요합니다.
- 로케일을 영어로 설정(en_US)하지 않으면 볼륨제어 등의 기능이 정상적으로 동작하지 않을 수도 있습니다.

활용방법
- media_player.play_media service 서비스 호출 시에, 현재 "media"로 지정한 미디어 타입만 지원 가능합니다.

HA 애드온
- 공식 VLC 애드온을 통한 VLC Media Player 도커이미지를 설치합니다.
- HA 로컬에 파일시스템에 미디어파일을 업로드 하여 재생할 수 있으며, configuration.yaml 파일에 해당 미디어 파일 경로가 지정되어 있어야 합니다.
