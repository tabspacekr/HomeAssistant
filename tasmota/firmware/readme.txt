tasmota custom firmware 제작을 위한 디렉터리

https://tasmota.github.io/docs/Compile-your-build/

Online Compilers~
Can only create a firmware binary. Use one of the tools to flash it to your device.

Gitpod - compile your own binary in the cloud using Gitpod.
- https://tasmota.github.io/docs/Gitpod/
TasmoCompiler - simple web GUI to compile Tasmota with your own settings
Simplest way to compile is with GitPod, requires only a web browser.

Once you have set up the development environment, unzip the source code into a folder.

8ch relay

backup_20220105_173021.bin
- sonoff zigbee bridge original firmware backup

===================================================================================

tasmota 초기화
- https://tasmota.github.io/docs/Device-Recovery/

하드리셋은 
ⓐ 버튼40초 누르기 
ⓑ 30초간 물리적인 전원off 완전꺼진상태에서(릴레이로 인입되는 파워소스차단) 10초내에 on/off 상태를 6번간 진행 후 7번째에 전원on상태로 유지 (별도의 poweronstate설정을 하지 않았을경우 전원인가시에 off상태임. 토글수행하면 1on/2off/3on/4off/5on/6off/7on 으로 되며 마지막에 on된 상태에서 reset됨)

tasmota soft reset (설정정보 유지한상태에서 wifi 접속네트워크만 재설정)
- 물리버튼 5회간 빠르게 누르면 tasmota가 ap모드로 전환되며, wifi재설정 가능
