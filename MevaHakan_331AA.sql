-- MySQL dump 10.13  Distrib 8.0.18, for macos10.14 (x86_64)
--
-- Host: localhost    Database: ProiectBD
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Angajat`
--

DROP TABLE IF EXISTS `Angajat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Angajat` (
  `AngajatID` int(11) NOT NULL AUTO_INCREMENT,
  `Nume` varchar(45) NOT NULL,
  `Prenume` varchar(45) NOT NULL,
  `CNP` decimal(13,0) NOT NULL,
  `Strada` varchar(45) NOT NULL,
  `OrasResedinta` varchar(45) NOT NULL,
  `JudetResedinta` varchar(45) NOT NULL,
  `DataNasterii` datetime DEFAULT NULL,
  `DataAngajarii` datetime NOT NULL,
  `Salariu` int(11) NOT NULL,
  `Sex` varchar(1) NOT NULL,
  `Username` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`AngajatID`),
  UNIQUE KEY `CNP_UNIQUE` (`CNP`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Angajat`
--

LOCK TABLES `Angajat` WRITE;
/*!40000 ALTER TABLE `Angajat` DISABLE KEYS */;
INSERT INTO `Angajat` VALUES (1,'Popescu','Ion',100000000000,'Unirii 20','Bucuresti','Bucuresti','1980-10-10 00:00:00','2017-10-10 00:00:00',2400,'M','Popescu','Ion'),(2,'Darius','Marian',1090000000000,'Economu 35','Constanta','Constanta','1990-11-11 00:00:00','2018-06-05 00:00:00',4000,'M','Darius','Marian'),(5,'Felicia','Mariana',120000000000,'Florilor 3','Tulcea','Constanta','1970-04-20 00:00:00','2005-01-01 00:00:00',6500,'F','Felicia','Mariana'),(6,'Guta','Florin',1375892745613,'Independentei 20','Bucuresti','Bucuresti','1995-04-04 00:00:00','2018-03-03 00:00:00',2800,'M','Guta','Florin'),(7,'Ion','Maria',987654321234,'Magnoliei 2','Chiajna','Bucuresti','1968-02-25 00:00:00','2010-06-02 00:00:00',3500,'F','Ion','Maria'),(8,'Marian','Popescu',1234565432467,'Marianelor 2','Constanta','Constanta','1990-02-02 00:00:00','2012-02-02 00:00:00',2000,'M','marius23','mariusss'),(9,'Kim','Kardashian',1987657890234,'West Hollywood 10','Hidden  Hills','California','1980-03-03 00:00:00','2014-05-05 00:00:00',4000,'F','kimmy45','kanyewest22');
/*!40000 ALTER TABLE `Angajat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Echipamente`
--

DROP TABLE IF EXISTS `Echipamente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Echipamente` (
  `EchipamentID` int(11) NOT NULL AUTO_INCREMENT,
  `ServiciuID` int(11) NOT NULL,
  `NumeEchipament` varchar(45) NOT NULL,
  `Cantitate` int(11) DEFAULT NULL,
  `DataRevizie` datetime DEFAULT NULL,
  PRIMARY KEY (`EchipamentID`),
  UNIQUE KEY `NumeEchipament_UNIQUE` (`NumeEchipament`),
  KEY `Serviciu_FK_idx` (`ServiciuID`),
  KEY `Serviciuu_FK_idx` (`ServiciuID`),
  CONSTRAINT `Serviciuu_FK` FOREIGN KEY (`ServiciuID`) REFERENCES `servicii` (`ServiciuID`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Echipamente`
--

LOCK TABLES `Echipamente` WRITE;
/*!40000 ALTER TABLE `Echipamente` DISABLE KEYS */;
INSERT INTO `Echipamente` VALUES (12,10,'Vopsea',20,NULL),(13,10,'Bidinea',5,NULL),(14,10,'Smirghel',5,NULL),(15,10,'Uscator',3,'2019-12-12 00:00:00'),(16,11,'Laptop',5,'2020-12-12 00:00:00'),(17,11,'Printer',5,'2020-12-12 00:00:00'),(18,12,'Ciocan',5,NULL),(19,12,'Surubelnita',10,NULL),(20,8,'Matura',10,NULL),(21,8,'Aspirator',5,'2020-12-12 00:00:00'),(22,8,'Galeata',5,NULL);
/*!40000 ALTER TABLE `Echipamente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Locatii`
--

DROP TABLE IF EXISTS `Locatii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Locatii` (
  `LocatieID` int(11) NOT NULL AUTO_INCREMENT,
  `AdresaLocatie` varchar(45) NOT NULL,
  `Oras` varchar(45) NOT NULL,
  `Judet` varchar(45) NOT NULL,
  `OraDeschidere` time NOT NULL,
  `OraInchidere` time NOT NULL,
  PRIMARY KEY (`LocatieID`),
  UNIQUE KEY `AdresaLocatie_UNIQUE` (`AdresaLocatie`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Locatii`
--

LOCK TABLES `Locatii` WRITE;
/*!40000 ALTER TABLE `Locatii` DISABLE KEYS */;
INSERT INTO `Locatii` VALUES (1,'Economu Cezarescu 52','Bucuresti','Bucuresti','09:00:00','18:00:00'),(2,'Dimitrie Pompeiu','Voluntari','Bucuresti','08:00:00','19:00:00'),(3,'Ecaterina Varga 20','Mangalia','Constanta','10:00:00','20:00:00'),(4,'Farului 35','Constanta','Constanta','08:00:00','21:00:00'),(5,'','','','00:00:00','00:00:00'),(9,'sdc','sadc','sadc','08:00:00','21:00:00'),(10,'Faget 22','Constanta','Constanta','08:00:00','21:00:00'),(11,'farului 1','Bucuresti','Bucuresti','09:00:00','18:00:00');
/*!40000 ALTER TABLE `Locatii` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Lucreaza`
--

DROP TABLE IF EXISTS `Lucreaza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Lucreaza` (
  `LucreazaID` int(11) NOT NULL AUTO_INCREMENT,
  `AngajatID` int(11) NOT NULL,
  `ProiectID` int(11) NOT NULL,
  `ServiciuID` int(11) NOT NULL,
  `DataIncepere` datetime NOT NULL,
  `NumarOre` int(11) NOT NULL,
  `Finalizat` int(11) DEFAULT '0',
  PRIMARY KEY (`LucreazaID`),
  KEY `Angajat_FK_idx` (`AngajatID`),
  KEY `Proiectt_FKK_idx` (`ProiectID`),
  KEY `Serv_FK_idx` (`ServiciuID`),
  CONSTRAINT `Angajat_FK` FOREIGN KEY (`AngajatID`) REFERENCES `angajat` (`AngajatID`),
  CONSTRAINT `Proiectt_FKK` FOREIGN KEY (`ProiectID`) REFERENCES `proiecte` (`ProiectID`),
  CONSTRAINT `Serv_FK` FOREIGN KEY (`ServiciuID`) REFERENCES `servicii` (`ServiciuID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Lucreaza`
--

LOCK TABLES `Lucreaza` WRITE;
/*!40000 ALTER TABLE `Lucreaza` DISABLE KEYS */;
INSERT INTO `Lucreaza` VALUES (11,1,1,8,'2019-12-02 00:00:00',4,1),(12,2,2,9,'2019-11-20 00:00:00',3,1),(13,5,3,10,'2019-12-01 00:00:00',4,1),(14,6,1,11,'2020-01-04 00:00:00',5,0);
/*!40000 ALTER TABLE `Lucreaza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proiecte`
--

DROP TABLE IF EXISTS `Proiecte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Proiecte` (
  `ProiectID` int(11) NOT NULL AUTO_INCREMENT,
  `Adresa` varchar(45) NOT NULL,
  `Oras` varchar(45) NOT NULL,
  `Judet` varchar(45) NOT NULL,
  `NumeProiect` varchar(45) NOT NULL,
  PRIMARY KEY (`ProiectID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proiecte`
--

LOCK TABLES `Proiecte` WRITE;
/*!40000 ALTER TABLE `Proiecte` DISABLE KEYS */;
INSERT INTO `Proiecte` VALUES (1,'Unirii 53','Bucuresti','Bucuresti','BlocNouUnirii'),(3,'Centura 50','Ploieste','Ploiesti','AdidasCentura');
/*!40000 ALTER TABLE `Proiecte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Servicii`
--

DROP TABLE IF EXISTS `Servicii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Servicii` (
  `ServiciuID` int(11) NOT NULL AUTO_INCREMENT,
  `LocatieID` int(11) NOT NULL,
  `NumeServiciu` varchar(20) NOT NULL,
  `PretServiciu/Ora` int(11) NOT NULL,
  PRIMARY KEY (`ServiciuID`),
  UNIQUE KEY `NumeServiciu_UNIQUE` (`NumeServiciu`),
  KEY `Locatie_FK_idx` (`LocatieID`),
  CONSTRAINT `Locatie_FK` FOREIGN KEY (`LocatieID`) REFERENCES `locatii` (`LocatieID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Servicii`
--

LOCK TABLES `Servicii` WRITE;
/*!40000 ALTER TABLE `Servicii` DISABLE KEYS */;
INSERT INTO `Servicii` VALUES (8,1,'Curatenie',25),(10,3,'Vopsire',60),(11,1,'Design',100),(12,2,'MontareMobila',30),(14,2,'GresieFaianta',60),(15,3,'IndreptarePereti',100);
/*!40000 ALTER TABLE `Servicii` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-15 20:20:44
