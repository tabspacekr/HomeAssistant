본 Code는 HA와 SmartIR의 Integration을 기반으로 동작합니다.

따라서, SmartIR 컴포넌트의 사전 설치가 필요하며
HA의 Configuration.yaml에 아래와 같이 Code선언 후에 사용할 수 있습니다.

smartir:
climate: !include climate.yaml
