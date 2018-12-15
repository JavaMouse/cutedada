# cutedada

### 数据库相关
1.创建库
CREATE DATABASE cutedada DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

2.USER表
DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `username` varchar(100) NOT NULL DEFAULT '' COMMENT '用户名',
  `password` varchar(200) NOT NULL DEFAULT '' COMMENT '密码',
  `nickname` varchar(100) DEFAULT NULL COMMENT '昵称',
  `is_admin` int(1) NOT NULL DEFAULT '0' COMMENT '是否管理员',
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `user` WRITE;

INSERT INTO `user` (`username`, `password`, `nickname`, `is_admin`)
VALUES
	('chennan','123123','陈楠',1),
	('tianbohao','123123','田博浩',1);

UNLOCK TABLES;


3.CHART表

DROP TABLE IF EXISTS `dada_chart`;

CREATE TABLE `dada_chart` (
  `id` varchar(100) NOT NULL DEFAULT '' COMMENT 'id',
  `dashboard_id` varchar(100) NOT NULL DEFAULT '' COMMENT 'dashboard_id',
  `chart_type` int(11) DEFAULT '1' COMMENT '1 折线图或柱状图 2 饼图 3 漏斗图',
  `title` varchar(3000) DEFAULT NULL COMMENT '图表标题',
  `x_data_sql` varchar(3000) DEFAULT NULL COMMENT 'x轴数据',
  `creater` varchar(100) DEFAULT NULL COMMENT '创建人',
  `demo` varchar(3000) DEFAULT NULL COMMENT '备注',
  `date_create` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `date_update` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `date_delete` datetime DEFAULT NULL COMMENT '删除时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `dada_chart` WRITE;

INSERT INTO `dada_chart` (`id`, `dashboard_id`, `chart_type`, `title`, `x_data_sql`, `creater`, `demo`, `date_create`, `date_update`, `date_delete`)
VALUES
	('chart_1','dashboard_1',1,'柱状图测试','select \n	province\nfrom\n	demo_data_weather\nwhere\n	province<>\'北京\'\ngroup by \n	province\norder by \n	province','tianbohao','这是一个测试柱状图','2018-12-15 16:08:41','2018-12-15 16:10:59',NULL),
	('chart_2','dashboard_1',2,'饼图测试',NULL,'tianbohao','这是一个测试饼图','2018-12-15 16:11:03','2018-12-15 16:11:31',NULL);
UNLOCK TABLES;

4.SERIES表

DROP TABLE IF EXISTS `dada_series`;

CREATE TABLE `dada_series` (
  `id` varchar(100) NOT NULL DEFAULT '',
  `chart_id` varchar(100) DEFAULT NULL,
  `series_name` varchar(100) DEFAULT NULL,
  `series_type` varchar(100) DEFAULT NULL,
  `data_sql` varchar(3000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `dada_series` WRITE;

INSERT INTO `dada_series` (`id`, `chart_id`, `series_name`, `series_type`, `data_sql`)
VALUES
	('series_1','chart_1','平均最高气温','line','select \n	avg(max_temp)\nfrom\n	demo_data_weather\nwhere\n	province<>\'北京\'\ngroup by \n	province\norder by \n	province'),
	('series_2','chart_1','平均最低气温','line','select \n	avg(min_temp)\nfrom\n	demo_data_weather\nwhere\n	province<>\'北京\'\ngroup by \n	province\norder by \n	province'),
	('series_3','chart_2','各省份数据条目','pie','select \n	province,count(1)\nfrom\n	demo_data_weather\ngroup by \n	province');

UNLOCK TABLES;



接口:
获取某个chart数据:
http://127.0.0.1:5000/chart/get_chart_info/<chart_id>
测试：
    柱状图、折线图：http://127.0.0.1:5000/chart/get_chart_info/chart_1
    饼图:http://127.0.0.1:5000/chart/get_chart_info/chart_2




