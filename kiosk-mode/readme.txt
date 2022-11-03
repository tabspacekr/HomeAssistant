# Lovelace Dashboard의 kiosk_mode 활성화를 위해서 js파일을 file upload 후, resource에 추가
# 이후 yaml 편집기에서 아래 코드를 추가하여 관리자가 아닌 사용자에게 search버튼이 노출되지 않도록 처리

title: tabspace
kiosk_mode:
  non_admin_settings:
    hide_search: true
views:
