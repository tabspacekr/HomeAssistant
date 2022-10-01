# 관리자 권한이 아닌 일반 사용자에게 좌측 sidebar의 History, Map, Media, Logbook, Energy를 접근 권한이 없도록 하며, 또한 매뉴자체에서 숨김처리를 하기 위한 수정방법
# docker환경의 경우, 해당 docker instance에 접근하여 처리하여야 하며, ha업데이트 시에 반영사항이 사라짐
# todo : ha naver map 소스 참고하여 sed replace shell 적용, 버전 업그레이드시에 
# https://community.home-assistant.io/t/admin-only-access-for-logbook-and-history-menus/187722/43
# https://github.com/home-assistant/core/blob/c5afaa2e6a1af77a69a0151dc1b8d7f5e3dcf2da/homeassistant/components/frontend/__init__.py#L262

docker exec -it homeassistant bash

# History
cp -a /usr/src/homeassistant/homeassistant/components/history /config/custom_components/history
cd /config/custom_components/history/
vi manifest.json
# 변경 후 코드
# {
#   "version": "2022.07.23",
#   "domain": "history",
#   ... etc
vi __init__.py
# 변경 후 코드
# frontend.async_register_built_in_panel(hass, "history", "history", "hass:chart-box", None, None, True)

# Map
cp -a /usr/src/homeassistant/homeassistant/components/map /config/custom_components/map
cd /config/custom_components/map/
vi manifest.json
# 변경 후 코드
# {
#   "version": "2022.08.7",
#   "domain": "history",
#   ... etc
vi __init__.py
# 변경 후 코드
# frontend.async_register_built_in_panel(hass, "map", "map", "hass:tooltip-account", None, None, True)

# Media
cp -a /usr/src/homeassistant/homeassistant/components/media_source /config/custom_components/media_source
cd /config/custom_components/media_source/
vi manifest.json
# 변경 후 코드
# {
#   "version": "2022.08.7",
#   "domain": "media_source",
#   ... etc
vi __init__.py
# 변경 후 코드
    # frontend.async_register_built_in_panel(                     
    #     hass, "media-browser", "media_browser", "hass:play-box-multiple", None, None, True
    # )

# Logbook
cp -a /usr/src/homeassistant/homeassistant/components/logbook /config/custom_components/logbook
cd /config/custom_components/logbook/
vi manifest.json
# 변경 후 코드
# {
#   "version": "2022.08.7",
#   "domain": "logbook",
#   ... etc
vi __init__.py
# 변경 후 코드
    # frontend.async_register_built_in_panel(
    #     hass, "logbook", "logbook", "hass:format-list-bulleted-type", None, None, True
    # ) 

# Energy
cp -a /usr/src/homeassistant/homeassistant/components/energy /config/custom_components/energy
cd /config/custom_components/energy/
vi manifest.json
# 변경 후 코드
# {
#   "version": "2022.08.7",
#   "domain": "energy",
#   ... etc
vi __init__.py
# 변경 후 코드
# frontend.async_register_built_in_panel(hass, DOMAIN, DOMAIN, "mdi:lightning-bolt", None, None, True)
