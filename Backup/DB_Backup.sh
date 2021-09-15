# Step1. 사전작업, 경로 생성 및 파일 생성
cd /
sudo mkdir backup
cd backup
sudo mkdir database_backup_files
sudo mkdir shell_script
cd shell_script
sudo vi db_backup_databases.txt
sudo vi db_backup.sh
sudo chmod a+x db_backup.sh

# Step2. 권한 정리
cd /
sudo chown ec2-user:ec2-user backup -R

# Step3. db_backup.shell 생성
# /backup/shell_script/db_backup.sh
#!/bin/bash

#======================================
# MySQL(MariaDB) DB Dump(=Backup) Script(Shell Type)
# 
# ceo@tabspace.kr 2021-08-29
#======================================

#======================================
# Def. Database List
#-------------------------------------------
# /backup/shell_script/db_backup_databases.txt
#===========================================

# Profile
# source /home/root/.profile

# Variable Declaration
BAK_FILE_NM=_db_backup_`date +"%Y%m%d-%H%M%S"`.sql
BAK_FILE_ZIP_NM=_db_backup_`date +"%Y%m%d-%H%M%S"`.tar.gz
BAK_LOG_FILE_NM=!db_backup_`date +"%Y%m%d-%H%M%S"`.log
BAK_FILE_SAVE_PATH=/backup/database_backup_files
BAK_FILE_DIRECTORY=`date +"%Y%m%d"`
WEEK_AGO=`date -d '1 week ago' +"%Y%m%d"`

MYSQL_HOST='localhost'
MYSQL_USER='root'
MYSQL_PASSWORD='REPLACE_YOUR_PASSWORD' 

# Create Backup Directory
mkdir ${BAK_FILE_SAVE_PATH}/${BAK_FILE_DIRECTORY}

# Start Backup
for backup_database in $(cat /backup/shell_script/db_backup_databases.txt);
do
        echo `date +"%Y-%m-%d %H:%M:%S"`" <<<"$backup_database" Backup Process Starting>>>" >> ${BAK_FILE_SAVE_PATH}/${BAK_FILE_DIRECTORY}/${BAK_LOG_FILE_NM}

        mysqldump --single-transaction --databases $backup_database -h ${MYSQL_HOST} -u ${MYSQL_USER} -p${MYSQL_PASSWORD} > ${BAK_FILE_SAVE_PATH}/${BAK_FILE_DIRECTORY}/$backup_database${BAK_FILE_NM} 2>&1 &&

        tar cvzfP ${BAK_FILE_SAVE_PATH}/${BAK_FILE_DIRECTORY}/$backup_database${BAK_FILE_ZIP_NM} ${BAK_FILE_SAVE_PATH}/${BAK_FILE_DIRECTORY}/$backup_database${BAK_FILE_NM} 2>&1 &&

        rm -rf ${BAK_FILE_SAVE_PATH}/${BAK_FILE_DIRECTORY}/$backup_database${BAK_FILE_NM} 2>&1 &&

        echo `date +"%Y-%m-%d %H:%M:%S"`" <<<"$backup_database" Backup Process Done>>>" >> ${BAK_FILE_SAVE_PATH}/${BAK_FILE_DIRECTORY}/${BAK_LOG_FILE_NM}
        echo "" >> ${BAK_FILE_SAVE_PATH}/${BAK_FILE_DIRECTORY}/${BAK_LOG_FILE_NM}
done

# 1 week ago backup delete
rm -rf $BAK_FILE_SAVE_PATH/$WEEK_AGO

# Step4. crontab 설정
crontab -e
0 5 * * * /backup/shell_script/db_backup.sh &

# Step5. crontab 시간대 변경
sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
sudo systemctl restart crond
# 만약 cron daemon을 재기동하지 않으면, 기존 utc기준으로 시간이 계산되어 오전5시가 아닌 한국시간 기준으로 오후2시(14시)에 명령이 실행됨
