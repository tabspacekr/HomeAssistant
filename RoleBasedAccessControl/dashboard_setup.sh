# https://community.home-assistant.io/t/admin-only-access-for-logbook-and-history-menus/187722/43
# https://github.com/home-assistant/core/blob/c5afaa2e6a1af77a69a0151dc1b8d7f5e3dcf2da/homeassistant/components/frontend/__init__.py#L262

docker exec -it homeassistant bash

# History
cp -a /usr/src/homeassistant/homeassistant/components/history /config/custom_components/history
cd /config/custom_components/history/
vi manifest.json
# {
#   "version": "2022.07.23",
#   "domain": "history",
#   ... etc
vi __init__.py
# frontend.async_register_built_in_panel(hass, "history", "history", "hass:chart-box", None, None, True)

# Map
cp -a /usr/src/homeassistant/homeassistant/components/map /config/custom_components/map
cd /config/custom_components/map/
vi manifest.json
# {
#   "version": "2022.08.7",
#   "domain": "history",
#   ... etc
vi __init__.py
frontend.async_register_built_in_panel(hass, "map", "map", "hass:tooltip-account", None, None, True)

# Media
cp -a /usr/src/homeassistant/homeassistant/components/media_source /config/custom_components/media_source
cd /config/custom_components/media_source/
vi manifest.json
# {
#   "version": "2022.08.7",
#   "domain": "media_source",
#   ... etc
vi __init__.py
    # frontend.async_register_built_in_panel(                     
    #     hass, "media-browser", "media_browser", "hass:play-box-multiple", None, None, True
    # )

#Logbook
cp -a /usr/src/homeassistant/homeassistant/components/logbook /config/custom_components/logbook
cd /config/custom_components/logbook/
vi manifest.json
# {
#   "version": "2022.08.7",
#   "domain": "logbook",
#   ... etc
vi __init__.py
    # frontend.async_register_built_in_panel(
    #     hass, "logbook", "logbook", "hass:format-list-bulleted-type", None, None, True
    # ) 

#Energy
cp -a /usr/src/homeassistant/homeassistant/components/energy /config/custom_components/energy
cd /config/custom_components/energy/
vi manifest.json
# {
#   "version": "2022.08.7",
#   "domain": "energy",
#   ... etc
vi __init__.py
# frontend.async_register_built_in_panel(hass, DOMAIN, DOMAIN, "mdi:lightning-bolt", None, None, True)
