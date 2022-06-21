https://www.home-assistant.io/integrations/vlc_telnet

VLC media player via Telnet
The vlc_telnet platform allows you to control a VLC media player using the built in telnet interface.

This service will control any instance of VLC player on the network with the telnet interface activated. To activate the telnet interface on your VLC Player please read the official VLC documentation. Also remember to add a firewall rule allowing inbound connections for the port used in the device running VLC.

In case the VLC is running on a host with a locale other than English, you may get some errors during the volume change. This is related to the different use of the decimal separator in other countries. Consider to set the locale to en_US before starting VLC.

Configuration
Adding VLC media player via Telnet to your Home Assistant instance can be done via the user interface, by using this My button:

Manual configuration steps
Services
When using the media_player.play_media service, only the “music” media type is supported for now.

Home Assistant Add-on
You can run a VLC Media Player on your Home Assistant installation using the official VLC add-on. Using it you can play files on the local network, Internet or files and playlist locally saved to the /share and /media folder of your Home Assistant installation.
