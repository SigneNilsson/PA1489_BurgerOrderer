-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 09, 2024 at 07:37 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `burger-orderer`
--

-- --------------------------------------------------------

--
-- Table structure for table `eidamburgare`
--

CREATE TABLE `eidamburgare` (
  `ID` int(11) NOT NULL,
  `ingredients` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `eidamburgare`
--

INSERT INTO `eidamburgare` (`ID`, `ingredients`) VALUES
(1, '\"bread\", \"meat\", \"cheddar\", \"pickle\", \"ranch mayo\", \"portabello mushroom\"');

-- --------------------------------------------------------

--
-- Table structure for table `mostafaburgare`
--

CREATE TABLE `mostafaburgare` (
  `ID` int(11) NOT NULL,
  `ingredients` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mostafaburgare`
--

INSERT INTO `mostafaburgare` (`ID`, `ingredients`) VALUES
(1, '\"bread\", \"plantbeef\", \"sauce\", \"onion\", \"salad\", \"tomato\", \"cucumber\"');

-- --------------------------------------------------------

--
-- Table structure for table `signeburgare`
--

CREATE TABLE `signeburgare` (
  `ID` int(11) NOT NULL,
  `ingredients` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `signeburgare`
--

INSERT INTO `signeburgare` (`ID`, `ingredients`) VALUES
(1, '\"bread\", \"halloumi\", \"sauce\", \"onion\", \"salad\", \"avocado\"');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `eidamburgare`
--
ALTER TABLE `eidamburgare`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `mostafaburgare`
--
ALTER TABLE `mostafaburgare`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `signeburgare`
--
ALTER TABLE `signeburgare`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `eidamburgare`
--
ALTER TABLE `eidamburgare`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `mostafaburgare`
--
ALTER TABLE `mostafaburgare`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `signeburgare`
--
ALTER TABLE `signeburgare`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
