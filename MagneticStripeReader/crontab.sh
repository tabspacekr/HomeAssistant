# 1분마다 실행 감시
*/1 * * * * /root/msr_kill_protect.sh >> /root/msr_kill_protect.log


# 적용 후 Crontab 재시작 (crontab -e로 하였으면 안해주어도됨)
# service crond restart
