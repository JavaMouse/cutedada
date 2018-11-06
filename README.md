# cutedada

### 数据库相关
1.创建库
CREATE DATABASE cutedada DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

2.表
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
