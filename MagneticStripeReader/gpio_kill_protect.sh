#! /bin/bash

## 환경설정
export PATH=/usr/local/bin:/usr/local/sbin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/bin

## 서비스 체크
# 출입통제기 GPIO 프로세스가 존재하는지 확인
# 만약 존재한다면 pid가 1로 반환될것임
export pid=`ps -ef |grep -v grep |grep "python3 -m mqtt_io /root/config.yml"| wc -l`

## 서비스 재시작
# pid값이 1인 경우에는 출입통제기 GPIO 서비스가 정상실행 상태

# 프로세스 정상 실행중인 경우
if [ "$pid" == 1 ]; then
        echo $(date)
        echo "출입통제기 GPIO 서비스 정상 실행 중" 
# 프로세스가 정상이 아닌 경우
else
        echo $(date)
        # 실행중인 GPIO 프로세스 이름으로 모두 강제 종료처리
        pkill -9 -f "python3 -m mqtt_io /root/config.yml" 
        # 백그라운드로 GPIO 프로세스 시작, nohup.out 안남기기 위해 /dev/null로 날림
        nohup su - root -c /root/mqtt-io.sh > /dev/null &
        echo "출입통제기 GPIO 서비스 재시작" 
fi
