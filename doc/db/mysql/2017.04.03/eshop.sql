/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : eshop

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2017-04-03 10:22:23
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
INSERT INTO `admin` VALUES ('2', 'admin', 'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', '2017-04-02 14:05:49.129088', '1', '2017-03-25 11:29:31.542917', '0');
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
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `password` varchar(150) NOT NULL,
  `nickname` varchar(30) DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `avatar` varchar(200) NOT NULL,
  `registTime` datetime(6) NOT NULL,
  `birthday` date DEFAULT NULL,
  `sex` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `truename` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES ('1', 'wdcxc!', '696ed12e9d81ec95308f7f31b6847778ed4443058c528b65dfaa2d9d5193e0da6c7af022b84a0e8781625bcd4a4fc3a5a6527c6e78c78ad5f210abe8131fa138', 'wdcxc', '15603005920', 'a@b.com', '/static/media/fileupload/customer/20170330/1490857498.593217_activity.jpg', '2017-03-30 02:41:38.169109', '2017-03-02', '1', '0', '*');

-- ----------------------------
-- Table structure for customer_collection
-- ----------------------------
DROP TABLE IF EXISTS `customer_collection`;
CREATE TABLE `customer_collection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `addTime` datetime(6) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer_collection
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
  `city` varchar(20) NOT NULL,
  `default` tinyint(1) NOT NULL,
  `dist` varchar(20) NOT NULL,
  `province` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer_receiveaddress
-- ----------------------------
INSERT INTO `customer_receiveaddress` VALUES ('4', '***???...111!!!!!!!', '156030', 'cxc', '2017-03-31 04:41:05.373843', '1', '揭阳市', '0', '榕城区', '广东');
INSERT INTO `customer_receiveaddress` VALUES ('5', 'nice', 'sss', '666', '2017-03-31 04:42:20.527636', '1', '日喀则地区', '1', '日喀则市', '西藏');

-- ----------------------------
-- Table structure for customer_shopcart
-- ----------------------------
DROP TABLE IF EXISTS `customer_shopcart`;
CREATE TABLE `customer_shopcart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `addTime` datetime(6) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_shopcart_customer_id_f207457c_fk_customer_id` (`customer_id`),
  KEY `customer_shopcart_product_id_a959c576_fk_product_id` (`product_id`),
  CONSTRAINT `customer_shopcart_customer_id_f207457c_fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `customer_shopcart_product_id_a959c576_fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer_shopcart
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
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;

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
INSERT INTO `django_migrations` VALUES ('42', 'models', '0002_collectionmodel', '2017-03-30 02:43:23.880159');
INSERT INTO `django_migrations` VALUES ('43', 'models', '0003_shopcartmodel', '2017-03-30 03:03:40.368763');
INSERT INTO `django_migrations` VALUES ('44', 'models', '0004_auto_20170330_1302', '2017-03-30 05:02:37.531718');
INSERT INTO `django_migrations` VALUES ('45', 'models', '0005_auto_20170331_0040', '2017-03-30 16:41:00.738807');
INSERT INTO `django_migrations` VALUES ('46', 'models', '0006_collectionmodel', '2017-03-30 16:59:13.902282');
INSERT INTO `django_migrations` VALUES ('47', 'models', '0002_auto_20170331_1801', '2017-03-31 10:01:59.177627');
INSERT INTO `django_migrations` VALUES ('48', 'models', '0003_auto_20170331_1928', '2017-03-31 11:29:27.756059');
INSERT INTO `django_migrations` VALUES ('49', 'models', '0002_auto_20170401_0935', '2017-04-01 01:35:42.789817');
INSERT INTO `django_migrations` VALUES ('50', 'models', '0003_collectionmodel', '2017-04-01 01:55:26.682305');
INSERT INTO `django_migrations` VALUES ('51', 'models', '0002_propertymetamodel_name', '2017-04-01 03:08:09.395166');
INSERT INTO `django_migrations` VALUES ('52', 'models', '0002_auto_20170401_1534', '2017-04-01 07:34:47.066931');
INSERT INTO `django_migrations` VALUES ('53', 'models', '0002_orderproductmodel', '2017-04-01 07:45:32.200762');
INSERT INTO `django_migrations` VALUES ('54', 'models', '0003_productmodel_status', '2017-04-01 08:05:00.128489');
INSERT INTO `django_migrations` VALUES ('55', 'models', '0004_orderproductmodel_egrade', '2017-04-01 08:10:15.308813');
INSERT INTO `django_migrations` VALUES ('56', 'models', '0005_productimagemodel', '2017-04-01 08:23:48.164135');
INSERT INTO `django_migrations` VALUES ('57', 'models', '0002_auto_20170402_2043', '2017-04-02 12:43:15.401931');
INSERT INTO `django_migrations` VALUES ('58', 'models', '0003_auto_20170402_2121', '2017-04-02 13:21:59.523598');
INSERT INTO `django_migrations` VALUES ('59', 'models', '0004_auto_20170402_2127', '2017-04-02 13:27:43.095471');
INSERT INTO `django_migrations` VALUES ('60', 'models', '0005_auto_20170402_2138', '2017-04-02 13:38:03.178423');
INSERT INTO `django_migrations` VALUES ('61', 'models', '0006_auto_20170402_2319', '2017-04-02 15:19:26.661592');
INSERT INTO `django_migrations` VALUES ('62', 'models', '0007_auto_20170403_1010', '2017-04-03 02:10:37.687337');

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
INSERT INTO `django_session` VALUES ('4z58f9u0x471b0bhuoj3vpt1e20dsuhc', 'NDY3MjY0NjI5MzQwZDExOGU4OWFkMDcwOTA2MGEwNGY3NGE0ZmU4Zjp7InVzZXIiOnsiYXBwIjoic2VsbGVyIiwiaWQiOjV9LCJfc2Vzc2lvbl9leHBpcnkiOjg2NDAwfQ==', '2017-04-02 07:23:58.117322');
INSERT INTO `django_session` VALUES ('a0c7v6wamqxnt4ki43y8ncolu42c99aj', 'ZWFkNmU4ZGM1NThiNDZjYWQwNmM2YjE5OWY5YTVjY2IwYjdiYWY2Yjp7Il9zZXNzaW9uX2V4cGlyeSI6ODY0MDAsInVzZXIiOnsiaWQiOjUsImFwcCI6InNlbGxlciJ9fQ==', '2017-04-03 11:43:23.798458');
INSERT INTO `django_session` VALUES ('g8d0vh9j0zmkhmver3147qz32y7exijb', 'MDI5N2UyNTE4NTJhN2JlOTgzNDcwODgzYmMzYjczY2IzZTVjNmEwZTp7Il9zZXNzaW9uX2V4cGlyeSI6ODY0MDAsImNhcHRjaGFDb2RlIjoiZHNwayJ9', '2017-03-30 13:52:33.552504');
INSERT INTO `django_session` VALUES ('g9kojloybyxv6gd5nlr0dr8pp2w0vbsi', 'NDY3MjY0NjI5MzQwZDExOGU4OWFkMDcwOTA2MGEwNGY3NGE0ZmU4Zjp7InVzZXIiOnsiYXBwIjoic2VsbGVyIiwiaWQiOjV9LCJfc2Vzc2lvbl9leHBpcnkiOjg2NDAwfQ==', '2017-04-04 02:18:26.865188');
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
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `payTime` datetime(6) DEFAULT NULL,
  `cancelTime` datetime(6) DEFAULT NULL,
  `customer_id` int(11) NOT NULL,
  `recevieAddress_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_customer_id_9da9253f_fk_customer_id` (`customer_id`),
  KEY `order_804ddc2f` (`recevieAddress_id`),
  CONSTRAINT `order_customer_id_9da9253f_fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `order_recevieAddress_id_b643c7b4_fk_customer_receiveaddress_id` FOREIGN KEY (`recevieAddress_id`) REFERENCES `customer_receiveaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order
-- ----------------------------

-- ----------------------------
-- Table structure for order_product
-- ----------------------------
DROP TABLE IF EXISTS `order_product`;
CREATE TABLE `order_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `sellPrice` decimal(10,2) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `sendTime` datetime(6) DEFAULT NULL,
  `receiveTime` datetime(6) DEFAULT NULL,
  `evaluateTime` datetime(6) DEFAULT NULL,
  `refundTime` datetime(6) DEFAULT NULL,
  `ACRefundTime` datetime(6) DEFAULT NULL,
  `refundReason` longtext,
  `evaluation` longtext,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `eGrade` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`),
  KEY `order_product_order_id_f65b4f18_fk_order_id` (`order_id`),
  KEY `order_product_seller_id_79f2b1b4_fk_seller_id` (`seller_id`),
  CONSTRAINT `order_product_order_id_f65b4f18_fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  CONSTRAINT `order_product_product_id_53139cb6_fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  CONSTRAINT `order_product_seller_id_79f2b1b4_fk_seller_id` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_product
-- ----------------------------

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `brand` varchar(50) NOT NULL,
  `amount` int(11) NOT NULL,
  `soldoutAmount` int(11) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `onShelveTime` datetime(6) DEFAULT NULL,
  `offShelveTime` datetime(6) DEFAULT NULL,
  `description` longtext,
  `category_id` int(11) DEFAULT NULL,
  `seller_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_category_id_640030a0_fk_product_category_id` (`category_id`),
  KEY `product_0a7c7ff2` (`seller_id`),
  CONSTRAINT `product_category_id_640030a0_fk_product_category_id` FOREIGN KEY (`category_id`) REFERENCES `product_category` (`id`),
  CONSTRAINT `product_seller_id_cb2471f5_fk_seller_id` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES ('2', '创维电视', '1000.00', '创维', '10', '0', '2017-04-02 13:39:08.051110', null, null, '很好很强大', '11', '5', '1');
INSERT INTO `product` VALUES ('3', 'TCL电视', '888.00', 'TCL', '1000', '0', '2017-04-02 13:40:15.213006', null, null, 'nice', '11', '5', '1');
INSERT INTO `product` VALUES ('6', '小米电视', '999.00', 'mi', '999', '0', '2017-04-02 13:50:17.153483', '2017-04-02 13:50:17.152986', null, '质优价廉', '13', '5', '1');

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
-- Table structure for product_consult
-- ----------------------------
DROP TABLE IF EXISTS `product_consult`;
CREATE TABLE `product_consult` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `askTime` datetime(6) NOT NULL,
  `replyTime` datetime(6) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_consult_customer_id_679d3d28_fk_customer_id` (`customer_id`),
  KEY `product_consult_9bea82de` (`product_id`),
  CONSTRAINT `product_consult_customer_id_679d3d28_fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `product_consult_product_id_6fcbc901_fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product_consult
-- ----------------------------

-- ----------------------------
-- Table structure for product_image
-- ----------------------------
DROP TABLE IF EXISTS `product_image`;
CREATE TABLE `product_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `order` int(11) NOT NULL,
  `url` varchar(200) NOT NULL,
  `addTime` datetime(6) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_image_product_id_8b9355c5_fk_product_id` (`product_id`),
  CONSTRAINT `product_image_product_id_8b9355c5_fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product_image
-- ----------------------------
INSERT INTO `product_image` VALUES ('3', null, '0', '/static/media/fileupload/product/20170402/1491138347.259849_activity1.jpg', '2017-04-02 13:39:08.124110', '2');
INSERT INTO `product_image` VALUES ('4', null, '0', '/static/media/fileupload/product/20170402/1491138347.27034_activity2.jpg', '2017-04-02 13:39:08.245497', '2');
INSERT INTO `product_image` VALUES ('5', null, '0', '/static/media/fileupload/product/20170402/1491140413.132042_commodity2.png', '2017-04-02 13:40:15.285489', '3');
INSERT INTO `product_image` VALUES ('6', null, '0', '/static/media/fileupload/product/20170402/1491140413.13604_commodity1.png', '2017-04-02 13:40:15.317571', '3');
INSERT INTO `product_image` VALUES ('7', null, '0', '/static/media/fileupload/product/20170402/1491141011.586569_ad1.jpg', '2017-04-02 13:50:17.438560', '6');

-- ----------------------------
-- Table structure for product_property
-- ----------------------------
DROP TABLE IF EXISTS `product_property`;
CREATE TABLE `product_property` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` varchar(50) NOT NULL,
  `meta_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_property_meta_id_452bf436_fk_product_property_meta_id` (`meta_id`),
  KEY `product_property_product_id_2b053f03_fk_product_id` (`product_id`),
  CONSTRAINT `product_property_meta_id_452bf436_fk_product_property_meta_id` FOREIGN KEY (`meta_id`) REFERENCES `product_property_meta` (`id`),
  CONSTRAINT `product_property_product_id_2b053f03_fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product_property
-- ----------------------------
INSERT INTO `product_property` VALUES ('1', '广州', '8', '2');
INSERT INTO `product_property` VALUES ('2', '4k', '9', '2');
INSERT INTO `product_property` VALUES ('3', '东莞', '8', '3');
INSERT INTO `product_property` VALUES ('4', '4K', '9', '3');

-- ----------------------------
-- Table structure for product_property_meta
-- ----------------------------
DROP TABLE IF EXISTS `product_property_meta`;
CREATE TABLE `product_property_meta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `addTime` datetime(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_property_met_category_id_b77c25d2_fk_product_category_id` (`category_id`),
  CONSTRAINT `product_property_met_category_id_b77c25d2_fk_product_category_id` FOREIGN KEY (`category_id`) REFERENCES `product_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product_property_meta
-- ----------------------------
INSERT INTO `product_property_meta` VALUES ('6', '2017-04-01 07:18:53.449634', '1', '产地');
INSERT INTO `product_property_meta` VALUES ('7', '2017-04-01 07:19:02.319242', '1', '分辨率');
INSERT INTO `product_property_meta` VALUES ('8', '2017-04-02 11:42:14.889536', '11', '产地');
INSERT INTO `product_property_meta` VALUES ('9', '2017-04-02 11:42:24.592162', '11', '分辨率');

-- ----------------------------
-- Table structure for seller
-- ----------------------------
DROP TABLE IF EXISTS `seller`;
CREATE TABLE `seller` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `password` varchar(150) DEFAULT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `truename` varchar(30) NOT NULL,
  `idno` varchar(18) NOT NULL,
  `registTime` datetime(6) NOT NULL,
  `shopAddress` varchar(100) NOT NULL,
  `shopName` varchar(30) NOT NULL,
  `thumbnail` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `idno` (`idno`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of seller
-- ----------------------------
INSERT INTO `seller` VALUES ('5', 'seller', '696ed12e9d81ec95308f7f31b6847778ed4443058c528b65dfaa2d9d5193e0da6c7af022b84a0e8781625bcd4a4fc3a5a6527c6e78c78ad5f210abe8131fa138', '15603005920', 'a@b.com', '', '123456789012345678', '2017-03-31 10:15:03.266385', '火星基地', '啥都卖小店', '/static/media/fileupload/seller/20170331/1490967221.610906_activity3.jpg');
INSERT INTO `seller` VALUES ('6', 'hahaha', 'd9e6762dd1c8eaf6d61b3c6192fc408d4d6d5f1176d0c29169bc24e71c3f274ad27fcd5811b313d681f7e55ec02d73d499c95455b6b5bb503acf574fba8ffe85', '15603005929', '1@2.com', '', '123456789012345679', '2017-04-03 02:10:54.523315', '', '', null);

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
