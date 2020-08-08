DROP DATABASE IF EXIST `Shop`;

CREATE DATABASE IF NOT EXISTS `Shop`;
SHOW DATABASES;
USE `Shop`;

CREATE TABLE IF NOT EXISTS `Product` (
    `ProductID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Name` VARCHAR(100),
    `Type` VARCHAR(100),
    `Price` FLOAT,
    `Count` INT,
    PRIMARY KEY (`ProductID`)
)ENGINE=InnoDB;


INSERT INTO Product(Name, Type, Price, Count)
VALUES ('Phone', 'Iphone', 450000.0, 5);

INSERT INTO Product(Name, Type, Price, Count)
VALUES ('Phone', 'Samsung', 300000.0, 10);

INSERT INTO Product(Name, Type, Price, Count)
VALUES ('Phone', 'REDMI', 200000.0, 20);



CREATE TABLE IF NOT EXISTS `Customer` (
    `CustomerID` INT UNSIGNED AUTO_INCREMENT,
    `Name` VARCHAR(100),
    `Phone` INT,
    `Password` VARCHAR(100),
    PRIMARY KEY(`CustomerID`)
)ENGINE=InnoDB;

INSERT INTO `Customer`(Name, Phone, Password)
VALUES ('Mike', 123456, 'sdjfjsd');

INSERT INTO `Customer`(Name, Phone, Password)
VALUES ('Nike', 12345687, 'jshgfhd');

INSERT INTO `Customer`(Name, Phone, Password)
VALUES ('John', 213454, 'asjhdjasgd');

CREATE TABLE IF NOT EXISTS `Order`(
    `OrderID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `CustomerID` INT REFERENCES Customer (CustomerID),
    `Date` Date,
    `ProductID` INT REFERENCES Product (ProductID),
    `TotalPrice` FLOAT,
    PRIMARY KEY (OrderID)

)ENGINE=InnoDB;

INSERT INTO `Order` (CustomerID , Date, ProductID, TotalPrice) VALUES (2, CURDATE() ,1 ,2000);
INSERT INTO `Order` (CustomerID , Date, ProductID, TotalPrice) VALUES (1, CURDATE() ,2 ,201);
SELECT Customer.Name, Product.Type ,Product.Price, Date  FROM `Order`
INNER JOIN Customer ON Order.CustomerID=Customer.CustomerID
INNER JOIN Product ON Order.ProductID=Product.ProductID;