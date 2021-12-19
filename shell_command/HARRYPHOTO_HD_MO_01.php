<?php
#mysql 접속 정보 기입
$conn = mysqli_connect("api.tabspace.kr", "changeme", "changeme_password", "changeme");
#데이터 insert를 위한 query
$sql  = "INSERT INTO flow_rate_check_daily(sensor_name, sensor_description, daily_date, timecreated) VALUES('HARRYPHOTO_HD_MO_01', '해리포토 홍대점 모션센서 1번', date_format(CURRENT_TIMESTAMP, '%Y-%m-%d'), CURRENT_TIMESTAMP);";
$result = mysqli_query($conn, $sql);
if($result === false){
            echo mysqli_error($conn);
}
?>
