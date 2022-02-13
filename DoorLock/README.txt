Keyless 및 IoT 스마트 도어락 제어를 위한 코드

마그네틱 카드 리더기(스캐너)도 지원합니다

dry contact(드라이 컨택) 형식을 지원하는 모든 도어락에 적용이 가능합니다.
- dry contact 형식은 현재 tasmota를 통한 접점제어로 처리중

bolt lock 방식 또한, 접점제어 형태로 적용 가능
- Electromagnetic Drop Bolt Lock
- 국내 구매처 사이트 / 모델명 GD-2000 / https://smartstore.naver.com/natureenc/products/5221207765?NaPm=ct%3Dktwmsq2g%7Cci%3D46176de7af3973ccb82c40c9288f39b8901a06a5%7Ctr%3Dslct%7Csn%3D2388872%7Chk%3Dedf87997b0d163504807770a7e71481acbbf4030

magnetic lock 방식 또한, 접점제어 형태로 적용 가능
- https://smartstore.naver.com/keps119/products/4588123209?NaPm=ct%3Dktwmyd00%7Cci%3D0zi0003gaiLvU0HPUvlK%7Ctr%3Dpla%7Chk%3D975a93eec325e290d6bd0fee6bbf052a631a9fae

sonoff re5v1c tasmota 적용 시 참고사항
- inching mode 설정이 필요함. (tasmota console에서 inching설정)
- 또는 automation에서 unlock 해제 시에 5초 뒤 다시 lock을 하는 형태로 구성
