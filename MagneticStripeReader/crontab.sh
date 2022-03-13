# 30초마다 실행 감시 (crontab은 1분이하로 설정이 불가능하여 30초 편법 구현)
* * * * * /root/msr_kill_protect.sh
* * * * * sleep 30; /root/msr_kill_protect.sh
#로그 사용 시 주석 해제
#* * * * * /root/msr_kill_protect.sh >> /root/msr_kill_protect.log
#* * * * * sleep 30; /root/msr_kill_protect.sh >> /root/msr_kill_protect.log   
# 부팅 시 자동실행
@reboot su - root -c /root/msr_kill_protect.sh
#로그 사용 시 주석 해제
#@reboot su - root -c /root/msr_kill_protect.sh >> /root/msr_kill_protect.log
