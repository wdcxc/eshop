/*
Navicat MySQL Data Transfer

Source Server         : eshop-mysql
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : eshop

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2017-03-24 09:58:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(130) NOT NULL,
  `grade` int(11) NOT NULL,
  `loginTime` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('2', 'admin', 'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', '999', '2017-03-23 09:02:18.900583');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add user', '1', 'add_user');
INSERT INTO `auth_permission` VALUES ('2', 'Can change user', '1', 'change_user');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete user', '1', 'delete_user');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('11', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('13', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('14', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete session', '5', 'delete_session');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(130) NOT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('1', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'admin', '0001_initial', '2017-03-22 15:44:35.653037');
INSERT INTO `django_migrations` VALUES ('2', 'admin', '0002_auto_20170303_1944', '2017-03-22 15:44:35.718446');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0003_auto_20170316_1445', '2017-03-22 15:44:35.824772');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0004_delete_adminmodel', '2017-03-22 15:44:36.096801');
INSERT INTO `django_migrations` VALUES ('5', 'app', '0001_initial', '2017-03-22 15:44:36.394577');
INSERT INTO `django_migrations` VALUES ('6', 'app', '0002_auto_20170316_2017', '2017-03-22 15:44:36.526235');
INSERT INTO `django_migrations` VALUES ('7', 'app', '0003_auto_20170317_2100', '2017-03-22 15:44:36.981592');
INSERT INTO `django_migrations` VALUES ('8', 'app', '0004_auto_20170317_2107', '2017-03-22 15:44:37.163034');
INSERT INTO `django_migrations` VALUES ('9', 'app', '0005_productcategorymodel_grade', '2017-03-22 15:44:37.715238');
INSERT INTO `django_migrations` VALUES ('10', 'app', '0006_auto_20170318_1123', '2017-03-22 15:44:37.839373');
INSERT INTO `django_migrations` VALUES ('11', 'app', '0007_auto_20170322_2327', '2017-03-22 15:44:38.180761');
INSERT INTO `django_migrations` VALUES ('12', 'contenttypes', '0001_initial', '2017-03-22 15:44:38.717820');
INSERT INTO `django_migrations` VALUES ('13', 'contenttypes', '0002_remove_content_type_name', '2017-03-22 15:44:39.824266');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0001_initial', '2017-03-22 15:44:50.879151');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0002_alter_permission_name_max_length', '2017-03-22 15:44:51.802779');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0003_alter_user_email_max_length', '2017-03-22 15:44:52.943006');
INSERT INTO `django_migrations` VALUES ('17', 'auth', '0004_alter_user_username_opts', '2017-03-22 15:44:53.034685');
INSERT INTO `django_migrations` VALUES ('18', 'auth', '0005_alter_user_last_login_null', '2017-03-22 15:44:53.724871');
INSERT INTO `django_migrations` VALUES ('19', 'auth', '0006_require_contenttypes_0002', '2017-03-22 15:44:53.751869');
INSERT INTO `django_migrations` VALUES ('20', 'auth', '0007_alter_validators_add_error_messages', '2017-03-22 15:44:53.798403');
INSERT INTO `django_migrations` VALUES ('21', 'auth', '0008_alter_user_username_max_length', '2017-03-22 15:44:54.574151');
INSERT INTO `django_migrations` VALUES ('22', 'customer', '0001_initial', '2017-03-22 15:44:55.017777');
INSERT INTO `django_migrations` VALUES ('23', 'customer', '0002_auto_20170220_1233', '2017-03-22 15:44:55.208062');
INSERT INTO `django_migrations` VALUES ('24', 'customer', '0003_auto_20170220_1711', '2017-03-22 15:44:56.466209');
INSERT INTO `django_migrations` VALUES ('25', 'customer', '0004_delete_customer', '2017-03-22 15:44:57.079488');
INSERT INTO `django_migrations` VALUES ('26', 'sessions', '0001_initial', '2017-03-22 15:44:58.053981');
INSERT INTO `django_migrations` VALUES ('27', 'models', '0001_initial', '2017-03-22 15:47:46.915383');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('tmc0wjw0pmc30n15wylptdapdfk8gaba', 'NGE4MTdkN2QyYjI0YWJkYjQzMzYwYjUxOGZmYzE0NGFkMmQ5OWVjYTp7InVzZXIiOnsibG9naW5UaW1lIjoiMjAxNy0wMy0yMyAxNzowMjoxOC45MDA1ODMiLCJpZCI6MiwibmFtZSI6ImFkbWluIn0sIl9zZXNzaW9uX2V4cGlyeSI6ODY0MDB9', '2017-03-24 11:33:28.471316');

-- ----------------------------
-- Table structure for index_carousel
-- ----------------------------
DROP TABLE IF EXISTS `index_carousel`;
CREATE TABLE `index_carousel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `show` tinyint(1) NOT NULL,
  `order` int(11) NOT NULL,
  `imgUrl` varchar(200) NOT NULL,
  `linkUrl` varchar(200) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of index_carousel
-- ----------------------------
INSERT INTO `index_carousel` VALUES ('1', '轮播1', '1', '1', '/static/media/fileupload/carousel/20170021/ad1.jpg', '/app/common/index', '2017-03-21 04:11:38.000000');
INSERT INTO `index_carousel` VALUES ('2', '轮播2', '2', '2', '/static/media/fileupload/carousel/20170021/ad2.jpg', '/app/common/index', '2017-03-21 04:14:29.000000');

-- ----------------------------
-- Table structure for product_category
-- ----------------------------
DROP TABLE IF EXISTS `product_category`;
CREATE TABLE `product_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parentId` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `order` int(11) NOT NULL,
  `grade` int(11) NOT NULL,
  `show` tinyint(1) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product_category
-- ----------------------------
INSERT INTO `product_category` VALUES ('1', '0', '家用电器', '2', '1', '1', '2017-03-21 04:19:27.000000');
INSERT INTO `product_category` VALUES ('2', '0', '医药保健', '1', '1', '1', '2017-03-21 04:19:55.000000');
INSERT INTO `product_category` VALUES ('3', '0', '运动、户外、钟表', '1', '1', '1', '2017-03-21 04:20:25.000000');
INSERT INTO `product_category` VALUES ('4', '1', '电视', '1', '2', '1', '2017-03-21 04:20:44.000000');
INSERT INTO `product_category` VALUES ('5', '1', '空调', '1', '2', '1', '2017-03-21 04:21:00.000000');
INSERT INTO `product_category` VALUES ('6', '1', '洗衣机', '1', '2', '1', '2017-03-21 04:21:07.000000');
INSERT INTO `product_category` VALUES ('7', '2', '中西药品', '1', '2', '1', '2017-03-21 04:21:58.000000');
INSERT INTO `product_category` VALUES ('8', '3', '运动鞋包', '1', '2', '1', '2017-03-21 04:22:40.000000');
INSERT INTO `product_category` VALUES ('9', '3', '运动服饰', '1', '2', '1', '2017-03-21 04:22:51.000000');
INSERT INTO `product_category` VALUES ('10', '8', '跑步鞋', '1', '3', '1', '2017-03-21 04:23:10.000000');
INSERT INTO `product_category` VALUES ('11', '4', '合资品牌', '1', '3', '1', '2017-03-21 04:23:30.000000');
INSERT INTO `product_category` VALUES ('12', '4', '国产品牌', '1', '3', '1', '2017-03-21 04:23:45.000000');
INSERT INTO `product_category` VALUES ('13', '4', '互联网品牌', '1', '3', '1', '2017-03-21 04:23:59.000000');

-- ----------------------------
-- Table structure for shoppingguide_channel
-- ----------------------------
DROP TABLE IF EXISTS `shoppingguide_channel`;
CREATE TABLE `shoppingguide_channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `addAdminId` int(11) NOT NULL,
  `show` tinyint(1) NOT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shoppingguide_channel
-- ----------------------------
INSERT INTO `shoppingguide_channel` VALUES ('1', '家用电器', '2017-03-23 10:37:56.825472', '2', '1', '1');
INSERT INTO `shoppingguide_channel` VALUES ('3', '运动户外', '2017-03-23 10:40:19.425032', '2', '1', '1');

-- ----------------------------
-- Table structure for shoppingguide_product
-- ----------------------------
DROP TABLE IF EXISTS `shoppingguide_product`;
CREATE TABLE `shoppingguide_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parentId` int(11) NOT NULL,
  `productId` int(11) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `addAdminId` int(11) NOT NULL,
  `show` tinyint(1) NOT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shoppingguide_product
-- ----------------------------

-- ----------------------------
-- Table structure for shoppingguide_subchannel
-- ----------------------------
DROP TABLE IF EXISTS `shoppingguide_subchannel`;
CREATE TABLE `shoppingguide_subchannel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `parentId` int(11) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `addAdminId` int(11) NOT NULL,
  `show` tinyint(1) NOT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shoppingguide_subchannel
-- ----------------------------
