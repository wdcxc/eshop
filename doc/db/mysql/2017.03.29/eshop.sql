/*
Navicat MySQL Data Transfer

Source Server         : eshop-mysql
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : eshop

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2017-03-29 22:02:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(200) NOT NULL,
  `loginTime` datetime(6) DEFAULT NULL,
  `root` tinyint(1) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `addAdminId` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('2', 'admin', 'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', '2017-03-28 11:26:07.184086', '1', '2017-03-25 11:29:31.542917', '0');
INSERT INTO `admin` VALUES ('9', 'test', 'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff', '2017-03-27 13:42:32.194601', '0', '2017-03-26 15:50:38.316031', '2');
INSERT INTO `admin` VALUES ('10', 'root', '99adc231b045331e514a516b4b7680f588e3823213abe901738bc3ad67b2f6fcb3c64efb93d18002588d3ccc1a49efbae1ce20cb43df36b38651f11fa75678e8', null, '1', '2017-03-26 15:50:55.918497', '2');

-- ----------------------------
-- Table structure for admin_group
-- ----------------------------
DROP TABLE IF EXISTS `admin_group`;
CREATE TABLE `admin_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `addAdminId` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin_group
-- ----------------------------
INSERT INTO `admin_group` VALUES ('14', '管理员管理', '2017-03-26 04:19:32.320862', '2');
INSERT INTO `admin_group` VALUES ('16', '顾客管理', '2017-03-27 13:32:51.874387', '2');
INSERT INTO `admin_group` VALUES ('17', '商城管理', '2017-03-27 13:33:05.315392', '2');
INSERT INTO `admin_group` VALUES ('18', '商家管理', '2017-03-27 13:33:27.443400', '2');
INSERT INTO `admin_group` VALUES ('19', '商品管理', '2017-03-27 13:33:39.773406', '2');

-- ----------------------------
-- Table structure for admin_groups
-- ----------------------------
DROP TABLE IF EXISTS `admin_groups`;
CREATE TABLE `admin_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `adminmodel_id` int(11) NOT NULL,
  `groupmodel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_groups_adminmodel_id_groupmodel_id_5d5ce45a_uniq` (`adminmodel_id`,`groupmodel_id`),
  KEY `admin_groups_groupmodel_id_aae14b79_fk_admin_group_id` (`groupmodel_id`),
  CONSTRAINT `admin_groups_adminmodel_id_4f0c49b8_fk_admin_id` FOREIGN KEY (`adminmodel_id`) REFERENCES `admin` (`id`),
  CONSTRAINT `admin_groups_groupmodel_id_aae14b79_fk_admin_group_id` FOREIGN KEY (`groupmodel_id`) REFERENCES `admin_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin_groups
-- ----------------------------
INSERT INTO `admin_groups` VALUES ('5', '2', '14');
INSERT INTO `admin_groups` VALUES ('18', '9', '17');
INSERT INTO `admin_groups` VALUES ('17', '10', '14');

-- ----------------------------
-- Table structure for admin_group_nodes
-- ----------------------------
DROP TABLE IF EXISTS `admin_group_nodes`;
CREATE TABLE `admin_group_nodes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groupmodel_id` int(11) NOT NULL,
  `nodemodel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_group_nodes_groupmodel_id_nodemodel_id_99a19a8c_uniq` (`groupmodel_id`,`nodemodel_id`),
  KEY `admin_group_nodes_nodemodel_id_ba83aee3_fk_admin_node_id` (`nodemodel_id`),
  CONSTRAINT `admin_group_nodes_groupmodel_id_0e69ac53_fk_admin_group_id` FOREIGN KEY (`groupmodel_id`) REFERENCES `admin_group` (`id`),
  CONSTRAINT `admin_group_nodes_nodemodel_id_ba83aee3_fk_admin_node_id` FOREIGN KEY (`nodemodel_id`) REFERENCES `admin_node` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin_group_nodes
-- ----------------------------
INSERT INTO `admin_group_nodes` VALUES ('5', '14', '1');
INSERT INTO `admin_group_nodes` VALUES ('7', '14', '2');
INSERT INTO `admin_group_nodes` VALUES ('8', '17', '3');
INSERT INTO `admin_group_nodes` VALUES ('9', '17', '5');
INSERT INTO `admin_group_nodes` VALUES ('10', '19', '6');

-- ----------------------------
-- Table structure for admin_node
-- ----------------------------
DROP TABLE IF EXISTS `admin_node`;
CREATE TABLE `admin_node` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `controller` varchar(30) NOT NULL,
  `action` varchar(30) NOT NULL,
  `linkUrl` varchar(200) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `addAdminId` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin_node
-- ----------------------------
INSERT INTO `admin_node` VALUES ('1', '管理员管理-添加节点', 'adminadmin', 'addNode', '/admin/adminadmin/addNode', '2017-03-25 12:07:07.721655', '0');
INSERT INTO `admin_node` VALUES ('2', '管理员管理-修改节点', 'adminadmin', 'updateNode', '/admin/adminadmin/updateNode', '2017-03-25 12:07:59.183204', '0');
INSERT INTO `admin_node` VALUES ('3', '商城管理-商城首页添加轮播图', 'appadmin', 'addCarousel', '/admin/appadmin/addCarousel', '2017-03-26 14:03:25.382808', '2');
INSERT INTO `admin_node` VALUES ('5', '商城管理-首页', 'appadmin', 'index', '/admin/appadmin/index', '2017-03-27 13:34:32.464425', '2');
INSERT INTO `admin_node` VALUES ('6', '商品管理-首页', 'productadmin', 'index', '/admin/productadmin/index', '2017-03-27 13:35:10.942440', '2');

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
-- Table structure for customer_receiveaddress
-- ----------------------------
DROP TABLE IF EXISTS `customer_receiveaddress`;
CREATE TABLE `customer_receiveaddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(100) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer_receiveaddress
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
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;

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
INSERT INTO `django_migrations` VALUES ('28', 'models', '0002_auto_20170324_2237', '2017-03-24 14:38:15.409321');
INSERT INTO `django_migrations` VALUES ('29', 'models', '0003_auto_20170324_2238', '2017-03-24 14:38:15.558652');
INSERT INTO `django_migrations` VALUES ('30', 'models', '0004_auto_20170325_1929', '2017-03-25 11:29:38.372250');
INSERT INTO `django_migrations` VALUES ('31', 'models', '0005_auto_20170326_1840', '2017-03-26 10:40:14.097616');
INSERT INTO `django_migrations` VALUES ('32', 'models', '0006_auto_20170326_1856', '2017-03-26 10:56:21.074494');
INSERT INTO `django_migrations` VALUES ('33', 'models', '0007_auto_20170326_1913', '2017-03-26 11:14:05.529329');
INSERT INTO `django_migrations` VALUES ('34', 'models', '0008_auto_20170326_2302', '2017-03-26 15:02:26.140908');
INSERT INTO `django_migrations` VALUES ('35', 'models', '0009_seller', '2017-03-29 02:15:05.798487');
INSERT INTO `django_migrations` VALUES ('36', 'models', '0010_auto_20170329_1049', '2017-03-29 02:51:10.000418');
INSERT INTO `django_migrations` VALUES ('37', 'models', '0011_auto_20170329_1050', '2017-03-29 02:51:11.362450');
INSERT INTO `django_migrations` VALUES ('38', 'models', '0012_auto_20170329_1059', '2017-03-29 02:59:59.601133');
INSERT INTO `django_migrations` VALUES ('39', 'models', '0002_auto_20170329_1601', '2017-03-29 08:01:34.463778');
INSERT INTO `django_migrations` VALUES ('40', 'models', '0002_customermodel_level', '2017-03-29 13:27:35.257047');
INSERT INTO `django_migrations` VALUES ('41', 'models', '0001_initial', '2017-03-29 13:50:21.375773');

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
INSERT INTO `django_session` VALUES ('g8d0vh9j0zmkhmver3147qz32y7exijb', 'MDI5N2UyNTE4NTJhN2JlOTgzNDcwODgzYmMzYjczY2IzZTVjNmEwZTp7Il9zZXNzaW9uX2V4cGlyeSI6ODY0MDAsImNhcHRjaGFDb2RlIjoiZHNwayJ9', '2017-03-30 13:52:33.552504');
INSERT INTO `django_session` VALUES ('tmc0wjw0pmc30n15wylptdapdfk8gaba', 'ZTNkMWJiMzMzZWFiNGY5Y2RmYzg4ZWZiODBmYTQyMTk4NGUxNDBmMDp7Il9zZXNzaW9uX2V4cGlyeSI6ODY0MDAsInVzZXIiOnsiaWQiOjIsImxvZ2luVGltZSI6IjIwMTctMDMtMjggMTk6MjY6MDcuMTg0MDg2IiwidXNlcm5hbWUiOiJhZG1pbiJ9fQ==', '2017-03-29 11:26:11.663969');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shoppingguide_channel
-- ----------------------------
INSERT INTO `shoppingguide_channel` VALUES ('1', '家用电器', '2017-03-23 10:37:56.825472', '2', '1', '1');

-- ----------------------------
-- Table structure for shoppingguide_product
-- ----------------------------
DROP TABLE IF EXISTS `shoppingguide_product`;
CREATE TABLE `shoppingguide_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parentId` int(11) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `addAdminId` int(11) NOT NULL,
  `show` tinyint(1) NOT NULL,
  `order` int(11) NOT NULL,
  `description` varchar(100) NOT NULL,
  `linkUrl` varchar(200) NOT NULL,
  `name` varchar(50) NOT NULL,
  `productImgUrl` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shoppingguide_product
-- ----------------------------
INSERT INTO `shoppingguide_product` VALUES ('2', '6', '2017-03-24 15:13:48.713999', '2', '1', '1', 'nice', 'www.baidu.com', '液晶电视', '/static/media/fileupload/shoppingguide/20170024/activity2.jpg');

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shoppingguide_subchannel
-- ----------------------------
INSERT INTO `shoppingguide_subchannel` VALUES ('6', '电视', '1', '2017-03-24 09:24:35.337573', '2', '1', '1');
