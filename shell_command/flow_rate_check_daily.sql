CREATE TABLE `flow_rate_check_daily` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'unique id\n',
  `sensor_name` varchar(50) NOT NULL COMMENT '센서명n',
  `sensor_description` varchar(50) DEFAULT NULL COMMENT '센서 상세 설명',
  `daily_date` datetime NOT NULL COMMENT '오늘날짜 ex.2021-11-12',
  `timecreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT '유닉스타임',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88510 DEFAULT CHARSET=utf8mb4;
