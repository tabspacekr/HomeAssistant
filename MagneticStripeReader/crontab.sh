# 1초마다 실행 감시 (crontab은 1분이하로 설정이 불가능하여 sleep으로 구현)
* * * * * /root/msr_kill_protect.sh
* * * * * sleep 1; /root/msr_kill_protect.sh
* * * * * sleep 2; /root/msr_kill_protect.sh
* * * * * sleep 3; /root/msr_kill_protect.sh
* * * * * sleep 4; /root/msr_kill_protect.sh
* * * * * sleep 5; /root/msr_kill_protect.sh
* * * * * sleep 6; /root/msr_kill_protect.sh
* * * * * sleep 7; /root/msr_kill_protect.sh
* * * * * sleep 8; /root/msr_kill_protect.sh
* * * * * sleep 9; /root/msr_kill_protect.sh
* * * * * sleep 10; /root/msr_kill_protect.sh
* * * * * sleep 11; /root/msr_kill_protect.sh
* * * * * sleep 12; /root/msr_kill_protect.sh
* * * * * sleep 13; /root/msr_kill_protect.sh
* * * * * sleep 14; /root/msr_kill_protect.sh
* * * * * sleep 15; /root/msr_kill_protect.sh
* * * * * sleep 16; /root/msr_kill_protect.sh
* * * * * sleep 17; /root/msr_kill_protect.sh
* * * * * sleep 18; /root/msr_kill_protect.sh
* * * * * sleep 19; /root/msr_kill_protect.sh
* * * * * sleep 20; /root/msr_kill_protect.sh
* * * * * sleep 21; /root/msr_kill_protect.sh
* * * * * sleep 22; /root/msr_kill_protect.sh
* * * * * sleep 23; /root/msr_kill_protect.sh
* * * * * sleep 24; /root/msr_kill_protect.sh
* * * * * sleep 25; /root/msr_kill_protect.sh
* * * * * sleep 26; /root/msr_kill_protect.sh
* * * * * sleep 27; /root/msr_kill_protect.sh
* * * * * sleep 28; /root/msr_kill_protect.sh
* * * * * sleep 29; /root/msr_kill_protect.sh
* * * * * sleep 30; /root/msr_kill_protect.sh
* * * * * sleep 31; /root/msr_kill_protect.sh
* * * * * sleep 32; /root/msr_kill_protect.sh
* * * * * sleep 33; /root/msr_kill_protect.sh
* * * * * sleep 34; /root/msr_kill_protect.sh
* * * * * sleep 35; /root/msr_kill_protect.sh
* * * * * sleep 36; /root/msr_kill_protect.sh
* * * * * sleep 37; /root/msr_kill_protect.sh
* * * * * sleep 38; /root/msr_kill_protect.sh
* * * * * sleep 39; /root/msr_kill_protect.sh
* * * * * sleep 40; /root/msr_kill_protect.sh
* * * * * sleep 41; /root/msr_kill_protect.sh
* * * * * sleep 42; /root/msr_kill_protect.sh
* * * * * sleep 43; /root/msr_kill_protect.sh
* * * * * sleep 44; /root/msr_kill_protect.sh
* * * * * sleep 45; /root/msr_kill_protect.sh
* * * * * sleep 46; /root/msr_kill_protect.sh
* * * * * sleep 47; /root/msr_kill_protect.sh
* * * * * sleep 48; /root/msr_kill_protect.sh
* * * * * sleep 49; /root/msr_kill_protect.sh
* * * * * sleep 50; /root/msr_kill_protect.sh
* * * * * sleep 51; /root/msr_kill_protect.sh
* * * * * sleep 52; /root/msr_kill_protect.sh
* * * * * sleep 53; /root/msr_kill_protect.sh
* * * * * sleep 54; /root/msr_kill_protect.sh
* * * * * sleep 55; /root/msr_kill_protect.sh
* * * * * sleep 56; /root/msr_kill_protect.sh
* * * * * sleep 57; /root/msr_kill_protect.sh
* * * * * sleep 58; /root/msr_kill_protect.sh
* * * * * sleep 59; /root/msr_kill_protect.sh
# disk full 방지를 위한 로그 삭제
0 * * * * cat /dev/null > /var/log/auth.log;cat /dev/null > /var/log/btmp >/dev/null 2>&1
# 5분마다 프로세스 
*/5 * * * * kill -9 `ps -ef | grep -v grep | grep 'python3 /root/mg.py' | awk '{print $2}'` >/dev/null 2>&1
# 부팅 시 자동실행
@reboot su - root -c /root/msr_kill_protect.sh
