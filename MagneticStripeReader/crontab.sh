# 1분마다 실행 감시
*/1 * * * * /root/msr_kill_protect.sh >> /root/msr_kill_protect.log 2>&1
# 부팅 시 자동실행
@reboot su - root -c /root/msr_kill_protect.sh >> /root/msr_kill_protect.log 2>&1

# 적용 후 Crontab 재시작 (crontab -e로 하였으면 안해주어도됨)
# service crond restart

# linux log 참고
# https://etloveguitar.tistory.com/m/20
