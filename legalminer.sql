-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: legalminer
-- ------------------------------------------------------
-- Server version	5.7.9-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `corporate`
--

DROP TABLE IF EXISTS `corporate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `corporate` (
  `corporate_url` varchar(255) NOT NULL,
  `corporate_name` varchar(100) DEFAULT NULL,
  `stock_id` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `link` varchar(45) DEFAULT NULL,
  `ipo_time` varchar(45) DEFAULT NULL,
  `principle` varchar(45) DEFAULT NULL,
  `industry` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`corporate_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corporate`
--

LOCK TABLES `corporate` WRITE;
/*!40000 ALTER TABLE `corporate` DISABLE KEYS */;
INSERT INTO `corporate` VALUES ('http://www.legalminer.com/corporate?id=557e914ba316485b68bbad22','中国民生银行股份有限公司','股票代码 上海主板600016','北京市西城区','010-68946790','http://www.cmbc.com.cn','上市时间：2000-12-19','法定代表人：洪崎','行业：货币金融服务'),('http://www.legalminer.com/corporate?id=557e914fa316485b68bbad32','招商银行股份有限公司','股票代码 上海主板600036','广东省深圳市福田区','0755-83195868','http://www.cmbchina.com','上市时间：2002-04-09','法定代表人：李建红','行业：货币金融服务'),('http://www.legalminer.com/corporate?id=557e924aa316485b68bbb05d','兴业银行股份有限公司','股票代码 上海主板601166','福建省福州市湖东路154号','0591-87824863','http://www.cib.com.cn','上市时间：2007-02-05','法定代表人：高建平','行业：货币金融服务'),('http://www.legalminer.com/corporate?id=557e924ea316485b68bbb071','中国农业银行股份有限公司','股票代码 上海主板601288','北京市东城区','010-85109619','http://www.abchina.com','上市时间：2010-07-15','法定代表人：刘士余','行业：货币金融服务'),('http://www.legalminer.com/corporate?id=557e924ea316485b68bbb075','交通银行股份有限公司','股票代码 上海主板601328','上海市浦东新区','021-58781234','http://www.bankcomm.com','上市时间：2007-05-15','法定代表人：牛锡明','行业：货币金融服务'),('http://www.legalminer.com/corporate?id=557e9254a316485b68bbb07e','中国工商银行股份有限公司','股票代码 上海主板601398','北京市西城区','010-66108608','http://www.icbc.com.cn','上市时间：2006-10-27','法定代表人：姜建清','行业：货币金融服务'),('http://www.legalminer.com/corporate?id=557e9264a316485b68bbb0a7','中国光大银行股份有限公司','股票代码 上海主板601818','北京市西城区','010-63636388','http://www.cebbank.com','上市时间：2010-08-18','法定代表人：唐双宁','行业：货币金融服务'),('http://www.legalminer.com/corporate?id=557e9266a316485b68bbb0b9','中国建设银行股份有限公司','股票代码 上海主板601939','北京市金融大街25号','010-66215533','http://www.ccb.com','上市时间：2007-09-25','法定代表人：王洪章','行业：货币金融服务'),('http://www.legalminer.com/corporate?id=557e9267a316485b68bbb0bf','中国银行股份有限公司','股票代码 上海主板601988','北京市复兴门内大街1号','010-66592638','http://www.boc.cn','上市时间：2006-07-05','法定代表人：田国立','行业：货币金融服务'),('http://www.legalminer.com/corporate?id=557e926aa316485b68bbb0c4','中信银行股份有限公司','股票代码 上海主板601998','北京市东城区','010-65558000','http://bank.ecitic.com','上市时间：2007-04-27','法定代表人：常振明','行业：货币金融服务');
/*!40000 ALTER TABLE `corporate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `court`
--

DROP TABLE IF EXISTS `court`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `court` (
  `court_url` varchar(255) NOT NULL,
  `court_name` varchar(255) DEFAULT NULL,
  `case_number` int(11) DEFAULT NULL,
  PRIMARY KEY (`court_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='法院';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `court`
--

LOCK TABLES `court` WRITE;
/*!40000 ALTER TABLE `court` DISABLE KEYS */;
INSERT INTO `court` VALUES ('http://www.legalminer.com/court?id=56016ae9364a6808dc6d5868','北京市朝阳区人民法院',32476),('http://www.legalminer.com/court?id=56016ae9364a6808dc6d58a1','广东省广州市中级人民法院',34797),('http://www.legalminer.com/court?id=56016ae9364a6808dc6d58ae','广东省深圳市中级人民法院',35383),('http://www.legalminer.com/court?id=56016ae9364a6808dc6d5901','上海市第一中级人民法院',25318),('http://www.legalminer.com/court?id=56016ae9364a6808dc6d5909','上海市浦东新区人民法院',43759),('http://www.legalminer.com/court?id=56016ae9364a6808dc6d591c','深圳市宝安区人民法院',33900),('http://www.legalminer.com/court?id=56016ae9364a6808dc6d5927','天津市滨海新区人民法院',24702),('http://www.legalminer.com/court?id=56016ae9364a6808dc6d5966','重庆市第五中级人民法院',23446),('http://www.legalminer.com/court?id=56050e0f364a680d1ce164d0','义乌市人民法院',29744),('http://www.legalminer.com/court?id=56050e0f364a680d1ce164db','慈溪市人民法院',25109),('http://www.legalminer.com/court?id=56050e17364a680d1ce164f5','浙江省杭州市中级人民法院',25454),('http://www.legalminer.com/court?id=56050e18364a680d1ce164fb','瑞安市人民法院',34306),('http://www.legalminer.com/court?id=56050e18364a680d1ce164fe','浙江省温州市中级人民法院',22892),('http://www.legalminer.com/court?id=56050e18364a680d1ce16509','浙江省高级人民法院',24964),('http://www.legalminer.com/court?id=56050e19364a680d1ce16526','绍兴市越城区人民法院',28910),('http://www.legalminer.com/court?id=562a70a2364a680bd81f7390','江苏省南京市中级人民法院',29434),('http://www.legalminer.com/court?id=56725370758c2d0bb8b6fd52','河南省郑州市中级人民法院',23437),('http://www.legalminer.com/court?id=5672ef1f758c2d08d8ccb7b6','辽宁省沈阳市中级人民法院',22729),('http://www.legalminer.com/court?id=5672ef3d758c2d08d8ccb8ec','安徽省合肥市中级人民法院',26124),('http://www.legalminer.com/court?id=5673d253758c2d0a1061dca9','四川省成都市中级人民法院',23596);
/*!40000 ALTER TABLE `court` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `judge`
--

DROP TABLE IF EXISTS `judge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `judge` (
  `judge_url` varchar(255) NOT NULL,
  `judge_name` varchar(45) DEFAULT NULL,
  `court` varchar(100) DEFAULT NULL,
  `case_number` int(11) DEFAULT NULL,
  PRIMARY KEY (`judge_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='法官';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `judge`
--

LOCK TABLES `judge` WRITE;
/*!40000 ALTER TABLE `judge` DISABLE KEYS */;
INSERT INTO `judge` VALUES ('http://www.legalminer.com/judge?id=565fc367364a680c4841f8fe','吴炜','浙江省高级人民法院',8198),('http://www.legalminer.com/judge?id=565fc545364a680c4842c804','杜循','广东省韶关市中级人民法院',7842),('http://www.legalminer.com/judge?id=565fc55f364a680c4842d074','杨帆','广东省韶关市中级人民法院',8439),('http://www.legalminer.com/judge?id=565fc5f3364a680c4843134a','王华明','广东省韶关市中级人民法院',9082),('http://www.legalminer.com/judge?id=565fc63c364a680c4843319e','王绍桓','天津市第一中级人民法院',7450),('http://www.legalminer.com/judge?id=565fc792364a680c4843c5f3','钟素雅','广东省韶关市中级人民法院',8352),('http://www.legalminer.com/judge?id=566d0385758c2d0b98ed845b','龙新国','湖南省长沙市中级人民法院',8024),('http://www.legalminer.com/judge?id=5676fa4b758c2d0a2ca5250f','刀文兵','云南省昆明市中级人民法院',15322),('http://www.legalminer.com/judge?id=5676fa85758c2d0a2ca52947','张若楠','云南省昆明市中级人民法院',11067),('http://www.legalminer.com/judge?id=5676fb1f758c2d0a2ca532d6','褚玉春','云南省昆明市中级人民法院',12144);
/*!40000 ALTER TABLE `judge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lawfirm`
--

DROP TABLE IF EXISTS `lawfirm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lawfirm` (
  `law_firm_url` varchar(255) NOT NULL,
  `law_firm_name` varchar(255) NOT NULL,
  `law_firm_lawyer_number` int(11) DEFAULT NULL,
  `occupation_number` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `fax_number` varchar(45) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `case_number` int(11) DEFAULT NULL,
  `history` int(11) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `principle` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`law_firm_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='律所';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lawfirm`
--

LOCK TABLES `lawfirm` WRITE;
/*!40000 ALTER TABLE `lawfirm` DISABLE KEYS */;
INSERT INTO `lawfirm` VALUES ('http://www.legalminer.com/lawfirm?id=557a9e63a3161e1ae9322d5a','北京大成（上海）律师事务所',422,'23101200111193128','世纪大道100号上海环球金融中心24层',' 58785888',' 58786218','http://www.dachenglaw.com',2511,16,'16年','王汉齐'),('http://www.legalminer.com/lawfirm?id=557e49d6a316100c8f61cc1d','北京市盈科（广州）律师事务所',427,'24401201011068788','广东省广州市越秀区',' 020-66857288',' 020-66857289','www.yingkefirm.com',3225,7,'7年','牟晋军'),('http://www.legalminer.com/lawfirm?id=557e4aada316100c8f61ceaf','上海市锦天城律师事务所',652,'23101199920121031','花园石桥路33号花旗集团大厦14楼',' 61059000',' 61059100','http://www.allbrightlaw.com',1694,18,'18年','吴明德'),('http://www.legalminer.com/lawfirm?id=557e4be7a316100c8f61d1c9','广东广信君达律师事务所',434,'24401199320600846','广东省广州市天河区',' 02037181333',' 02037181388','未知',2903,24,'24年','王晓华'),('http://www.legalminer.com/lawfirm?id=55a780648a869dda561dc356','北京大成律师事务所',769,'21101199220250536','北京市朝阳区',' 58137799',' 58137788','http://www.dachenglaw.com',2129,25,'25年','彭雪峰'),('http://www.legalminer.com/lawfirm?id=55a780988a869dda561dc7f7','北京市中银律师事务所',492,'21101199310430833','北京市朝阳区',' 58698899',' 58699666','http://www.zhongyinlawyer.com',1958,24,'24年','李炬'),('http://www.legalminer.com/lawfirm?id=55a7809b8a869dda561dc83e','北京市金杜律师事务所',407,'21101199310089150','北京市朝阳区',' 58785588',' 58785599','http://www.kingandwood.com',418,24,'24年','王玲'),('http://www.legalminer.com/lawfirm?id=55a780aa8a869dda561dc9a6','北京市盈科律师事务所',587,'21101200110055052','北京市朝阳区',' 010-59626699',' 010-59626918','http://www.yingkelawyer.com/',5770,16,'16年','梅向荣'),('http://www.legalminer.com/lawfirm?id=565c1e85518305078801dcf4','河北甲信律师事务所',515,'21305200110408639','河北省邢台市桥西区',' 0319——2235541','未知','未知',368,16,'16年','闫泽平');
/*!40000 ALTER TABLE `lawfirm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lawyer`
--

DROP TABLE IF EXISTS `lawyer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lawyer` (
  `lawyer_url` varchar(255) NOT NULL,
  `lawyer_name` varchar(45) DEFAULT NULL,
  `occupation_number` varchar(255) DEFAULT NULL,
  `law_firm_name` varchar(255) DEFAULT NULL,
  `case_number` int(11) DEFAULT NULL,
  `history` int(11) DEFAULT NULL,
  `education` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`lawyer_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='律师';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lawyer`
--

LOCK TABLES `lawyer` WRITE;
/*!40000 ALTER TABLE `lawyer` DISABLE KEYS */;
/*!40000 ALTER TABLE `lawyer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-16 22:24:16
