HA와 외부시스템간의 연계처리를 위한 api 가이드 문서

- WebHook (API키 불필요)
- RestAPI (API키 필요)
- WebSocket (API키 필요)
- Camera_proxy and Camera_proxy_stream (API키 및 camera token 필요)

아두이노 코드를 활용한 시리얼통신의 경우 webhook을 통한 데이터 전송이 HA 데이터 연계에 가장 쉬운 방법으로 권장
- 단순한 센서데이터 (온도, 습도, 미세먼지농도, 조도 등)의 publish시에 간단하게 사용
- 단 webhook의 경우, token없이 url접근만으로 데이터를 변경 가능하기에 web hook url을 유추가 불가능하도록 랜덤하게 생성 권장. 주소 노출시에 취약한 점이 발생

복잡한 로직의 경우 shell_command로 ha에서 호출 후 사전 작성된 python code를 사용하는 방식을 권장
- 단, ha의 shell_command 적용을 위해 core restart가 필요
- shell command 경로 지정시 ha재기동 없이 sh파일만 수정하여 관리가능

OpenWeatherMap의 경우 API키 발행 후에 HA Integration에서 설정이 필요.

RestAPI는 swagger ui를 통해 테스트가 가능함
- https://api-docs.tabspace.kr
