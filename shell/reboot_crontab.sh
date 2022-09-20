# crontab -e
# 매월 15일 오전4시 정각에 재부팅 수행
0 4 15 * * reboot -f >/dev/null 2>&1
