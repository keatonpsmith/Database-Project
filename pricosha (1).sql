-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 07, 2018 at 10:28 AM
-- Server version: 5.7.21
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pricosha`
--

-- --------------------------------------------------------

--
-- Table structure for table `belong`
--

DROP TABLE IF EXISTS `belong`;
CREATE TABLE IF NOT EXISTS `belong` (
  `email` varchar(20) NOT NULL,
  `owner_email` varchar(20) NOT NULL,
  `fg_name` varchar(20) NOT NULL,
  PRIMARY KEY (`email`,`owner_email`,`fg_name`),
  KEY `owner_email` (`owner_email`,`fg_name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `belong`
--

INSERT INTO `belong` (`email`, `owner_email`, `fg_name`) VALUES
('AA@nyu.edu', 'AA@nyu.edu', 'family'),
('AA@nyu.edu', 'AA@nyu.edu', 'roommates'),
('BB@nyu.edu', 'BB@nyu.edu', 'family'),
('CC@nyu.edu', 'AA@nyu.edu', 'family'),
('DD@nyu.edu', 'AA@nyu.edu', 'family'),
('EE@nyu.edu', 'AA@nyu.edu', 'family'),
('EE@nyu.edu', 'BB@nyu.edu', 'family'),
('FF@nyu.edu', 'BB@nyu.edu', 'family'),
('GG@nyu.edu', 'AA@nyu.edu', 'roommates'),
('HH@nyu.edu', 'AA@nyu.edu', 'roommates');

-- --------------------------------------------------------

--
-- Table structure for table `contentitem`
--

DROP TABLE IF EXISTS `contentitem`;
CREATE TABLE IF NOT EXISTS `contentitem` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `email_post` varchar(20) DEFAULT NULL,
  `post_time` timestamp NULL DEFAULT NULL,
  `file_path` varchar(100) DEFAULT NULL,
  `item_name` varchar(20) DEFAULT NULL,
  `is_pub` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  KEY `email_post` (`email_post`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contentitem`
--

INSERT INTO `contentitem` (`item_id`, `email_post`, `post_time`, `file_path`, `item_name`, `is_pub`) VALUES
(1, 'AA@nyu.edu', '2018-11-20 17:00:00', NULL, 'Whiskers', 0),
(2, 'AA@nyu.edu', '2018-11-20 18:00:00', NULL, 'leftovers in fridge', 0),
(3, 'BB@nyu.edu', '2018-11-20 19:00:00', NULL, 'Rover', 0),
(4, 'AA@nyu.edu', '2018-11-20 14:00:00', NULL, 'Dirty Bathroom', 1),
(5, 'BB@nyu.edu', '2018-11-20 05:00:00', NULL, 'New House', 1),
(6, 'CC@nyu.edu', '2018-11-01 15:00:00', 'test', 'First Photo', 1),
(10, 'WW@nyu.edu', '2018-12-07 05:33:38', 'ign', 'test', 1),
(11, 'WW@nyu.edu', '2018-12-07 05:34:39', 'whocares', 'nottest', 0);

-- --------------------------------------------------------

--
-- Table structure for table `friendgroup`
--

DROP TABLE IF EXISTS `friendgroup`;
CREATE TABLE IF NOT EXISTS `friendgroup` (
  `owner_email` varchar(20) NOT NULL,
  `fg_name` varchar(20) NOT NULL,
  `description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`owner_email`,`fg_name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `friendgroup`
--

INSERT INTO `friendgroup` (`owner_email`, `fg_name`, `description`) VALUES
('AA@nyu.edu', 'family', NULL),
('BB@nyu.edu', 'family', NULL),
('AA@nyu.edu', 'roommates', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
CREATE TABLE IF NOT EXISTS `person` (
  `email` varchar(20) NOT NULL,
  `password` char(64) DEFAULT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `person`
--

INSERT INTO `person` (`email`, `password`, `fname`, `lname`) VALUES
('AA@nyu.edu', '58bb119c35513a451d24dc20ef0e9031ec85b35bfc919d263e7e5d9868909cb5', 'Ann', 'Anderson'),
('BB@nyu.edu', 'fc686c314491e1f68bf1899fc54b2327353c44dd1ab4ed56538ef623edd1e866', 'Bob', 'Baker'),
('CC@nyu.edu', 'a56362a10c816abf206d72cb914e2d5ca454eb9c7e744f88b1a1422c379e9942', 'Cathy', 'Chang'),
('DD@nyu.edu', '92f089f2a70df5d960aac7c83dac8bc454c2cb1fa9a8e3061a8f6a84f338f2d1', 'David', 'Davidson'),
('EE@nyu.edu', 'bd43c62d6ccc0ceb731444123576f0ee21f5f66bfd673edacd95e52e724b4fa6', 'Ellen', 'Ellenberg'),
('FF@nyu.edu', '096aa8510b0dc13190f1f237db8e29ad6ea34e2f779f2088c7826248535fbf6a', 'Fred', 'Fox'),
('GG@nyu.edu', 'bee30e5b6d59c1bdf10100ef331706553fd3c4e6b0a342a092c6f6f733b8be36', 'Gina', 'Gupta'),
('HH@nyu.edu', 'a417aa4975c55a9b975ccd869a6444593fee6fff2868bf7a5811509f66b7224d', 'Helen', 'Harper'),
('WW@nyu.edu', '13172f18b181afbba0fc520551918fee46304c1d2e6bc5a76d1bcc8c8af59f10', 'William', 'Wallace');

-- --------------------------------------------------------

--
-- Table structure for table `rate`
--

DROP TABLE IF EXISTS `rate`;
CREATE TABLE IF NOT EXISTS `rate` (
  `email` varchar(20) NOT NULL,
  `item_id` int(11) NOT NULL,
  `rate_time` timestamp NULL DEFAULT NULL,
  `emoji` varchar(20) CHARACTER SET utf8mb4 DEFAULT NULL,
  PRIMARY KEY (`email`,`item_id`),
  KEY `item_id` (`item_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rate`
--

INSERT INTO `rate` (`email`, `item_id`, `rate_time`, `emoji`) VALUES
('FF@nyu.edu', 3, '2018-11-21 01:35:00', ':)');

-- --------------------------------------------------------

--
-- Table structure for table `share`
--

DROP TABLE IF EXISTS `share`;
CREATE TABLE IF NOT EXISTS `share` (
  `owner_email` varchar(20) NOT NULL,
  `fg_name` varchar(20) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`owner_email`,`fg_name`,`item_id`),
  KEY `item_id` (`item_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `share`
--

INSERT INTO `share` (`owner_email`, `fg_name`, `item_id`) VALUES
('AA@nyu.edu', 'family', 1),
('AA@nyu.edu', 'roommates', 2),
('BB@nyu.edu', 'family', 3);

-- --------------------------------------------------------

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
CREATE TABLE IF NOT EXISTS `tag` (
  `email_tagged` varchar(20) NOT NULL,
  `email_tagger` varchar(20) NOT NULL,
  `item_id` int(11) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `tagtime` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`email_tagged`,`email_tagger`,`item_id`),
  KEY `email_tagger` (`email_tagger`),
  KEY `item_id` (`item_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tag`
--

INSERT INTO `tag` (`email_tagged`, `email_tagger`, `item_id`, `status`, `tagtime`) VALUES
('GG@nyu.edu', 'AA@nyu.edu', 2, 'True', '2018-11-20 20:00:00'),
('BB@nyu.edu', 'WW@nyu.edu', 11, 'False', '2018-12-05 08:00:00'),
('CC@nyu.edu', 'BB@nyu.edu', 10, 'False', '2018-12-04 05:15:00');

DROP TABLE IF EXISTS `comments`;
CREATE TABLE IF NOT EXISTS `comments`( 
  `commentor` varchar(20) NOT NULL, 
  `comment` varchar(25) NOT NULL,
  `item_id` int(11) NOT NULL, 
  `commenttime` timestamp NULL DEFAULT NULL, 
  PRIMARY KEY (`commentor`,`item_id`) 
  KEY `commentor` (`commentor`),
  KEY `item_id` (`item_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;