고퀄(헤이홈) 스마트 리모콘 허브 펌웨어 백업

tasmotizer의 backup기능이 정상적으로 동작하지 않아, esptool을 통한 백업 방식 사용

github repository: https://github.com/espressif/esptool
flashing tool (win64) : https://github.com/espressif/esptool/releases/download/v3.2/esptool-v3.2-win64.zip

#백업
esptool -b 115200 --port COM4 read_flash 0x000000 0x100000 flash_1M.bin

#복구
esptool -b 115200 --port COM4 write_flash --flash_freq 80m 0x000000 flash_1M.bin

#참고사이트
https://community.blynk.cc/t/how-to-backup-restore-official-firmware-on-any-espressif-esp8266-esp32/34309
