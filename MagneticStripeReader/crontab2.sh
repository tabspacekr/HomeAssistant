* * * * * su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 5; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 10; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 15; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 20; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 25; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 30; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 35; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 40; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 45; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 50; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 55; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 5; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 10; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 15; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 20; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 25; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 30; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 35; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 40; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 45; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 50; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 55; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
0 * * * * cat /dev/null > /var/log/auth.log;cat /dev/null > /var/log/btmp >/dev/null 2>&1
*/5 * * * * sleep 3; su - root -c /root/power_live.sh >/dev/null 2>&1
*/5 * * * * sleep 13; su - root -c pkill -9 -f "python3 /root/mg.py" 
@reboot su - root -c /root/hostname.sh
@reboot su - root -c /root/gpio_kill_protect.sh
@reboot su - root -c /root/msr_kill_protect.sh
@reboot su - root -c /root/power_on.sh
@reboot su - root -c /root/runonce.sh
