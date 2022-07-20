# m h  dom mon dow   command
* * * * * su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 3; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 6; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 9; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 12; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 15; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 18; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 21; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 24; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 27; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 30; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 33; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 36; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 39; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 42; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 45; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 48; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 51; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 54; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 57; su - root -c /root/msr_kill_protect.sh >/dev/null 2>&1
* * * * * su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 3; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 6; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 9; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 12; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 15; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 18; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 21; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 24; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 27; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 30; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 33; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 36; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 39; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 42; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 45; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 48; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 51; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 54; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
* * * * * sleep 57; su - root -c /root/gpio_kill_protect.sh >/dev/null 2>&1
0 * * * * cat /dev/null > /var/log/auth.log;cat /dev/null > /var/log/btmp >/dev/null 2>&1
*/5 * * * * sleep 13; su - root -c pkill -9 -f "python3 /root/mg.py" 
@reboot su - root -c /root/gpio_kill_protect.sh
@reboot su - root -c /root/msr_kill_protect.sh
@reboot python3 /root/boot_led.py
