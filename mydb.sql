-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 31, 2021 at 05:34 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inverter`
--

-- --------------------------------------------------------

--
-- Table structure for table `battery`
--

CREATE TABLE `battery` (
  `ID` int(11) NOT NULL,
  `product` int(11) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `voltage` decimal(20,6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `battery`
--

INSERT INTO `battery` (`ID`, `product`, `timestamp`, `voltage`) VALUES
(1, 1, '2021-08-29 06:45:55', '11.600000'),
(2, 1, '2021-08-29 06:59:52', '10.000000'),
(3, 1, '2021-10-11 15:19:50', '13.000000'),
(4, 2, '2021-10-11 15:20:04', '11.750000'),
(5, 1, '2021-10-11 15:20:16', '12.500000'),
(6, 1, '2021-10-12 10:15:44', '15.000000'),
(7, 2, '2021-10-12 10:19:57', '12.000000'),
(8, 1, '2021-10-12 15:02:32', '13.750000'),
(9, 1, '2021-10-30 08:51:00', '12.000000'),
(10, 1, '2021-10-30 11:01:47', '14.000000'),
(11, 1, '2021-10-31 02:56:53', '13.000000'),
(12, 2, '2021-10-31 03:04:13', '15.000000'),
(13, 1, '2021-10-31 11:46:18', '12.500000'),
(14, 1, '2021-10-31 12:19:53', '13.000000'),
(15, 1, '2021-10-31 12:29:33', '12.000000'),
(16, 1, '2021-10-31 12:46:14', '13.000000');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `product` int(11) NOT NULL,
  `user` varchar(50) NOT NULL DEFAULT '0',
  `address` varchar(50) NOT NULL DEFAULT '0',
  `last refill` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`product`, `user`, `address`, `last refill`) VALUES
(1, 'Ashwath', 'Ramamoorthy Avenue, Kolapakkam', '2020-09-19'),
(2, 'Gokul Palani', 'Madipakkam', '2020-10-27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `battery`
--
ALTER TABLE `battery`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`product`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `battery`
--
ALTER TABLE `battery`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `product` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
