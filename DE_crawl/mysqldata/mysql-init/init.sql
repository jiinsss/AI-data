
DROP DATABASE IF EXISTS `mysql-db`;

CREATE DATABASE `mysql-db`;

USE `mysql-db`;

DROP TABLE IF EXISTS `reviewtable`;
DROP TABLE IF EXISTS `imgtable`;

CREATE TABLE `reviewtable` (
  `시간` DATETIME,
  `유저네임` VARCHAR(20),
  `리뷰` VARCHAR(300),
  `점수` INT,
  `추천수` INT
  
);

CREATE TABLE `imgtable` (
  `게임이름` VARCHAR(20),
  `이미지_파일` longblob NOT NULL
);
