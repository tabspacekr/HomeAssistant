HA와 외부시스템간의 연계처리를 위한 api 가이드 문서

- WebHook (API키 불필요)
- RestAPI (API키 필요)
- WebSocket (API키 필요)
- Camera_proxy and Camera_proxy_stream (camera token 필요)

아두이노 코드를 활용한 시리얼통신의 경우 webhook을 통한 데이터 전송이 HA 데이터 연계에 가장 쉬운 방법으로 권장됩니다
단 webhook의 경우 주소 노출시에 취약한 점이 발생합니다.

복잡한 로직의 경우 shell_command로 ha에서 호출 후 사전 작성된 python code를 사용하는 편이 권장됩니다. ha의 shell_command 적용을 위해 core restart가 필요하기 때문입니다.


OpenWeatherMap의 경우 API키 발행 후에 HA Integration에서 설정이 필요합니다.
