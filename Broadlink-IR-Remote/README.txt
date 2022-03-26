본 Code는 Broadlink RM시리즈의 HA와 SmartIR의 Integration을 기반으로 동작합니다.

따라서, SmartIR 컴포넌트의 사전 설치가 필요하며
HA의 Configuration.yaml에 아래와 같이 Code선언 후에 사용할 수 있습니다.

smartir:
climate: !include climate.yaml

국내 유통되는 삼성/LG 모델 등에서 범용적으로 사용 가능합니다.
로컬 구성이 아닌 클라우드기반으로 HA가 설치된 경우에는 동작하지 않습니다.
- 사유 : smartir integration 에서 broadlink local control 기능은 ip기반 동작만 지원하기때문
