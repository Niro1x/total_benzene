CREATE TABLE petrolprice(
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    solarprice float NOT NULL,
    petrol80price float NOT NULL,
    petrol92price float NOT NULL,
    petrol95price float NOT NULL,
    CONSTRAINT PRIMARY PRIMARY KEY (date)
    
);

CREATE TABLE Employee(
    id INT AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    nationalID varchar(255) NOT NULL,
    phoneNumber varchar(255) NOT NULL,
    job varchar(255) NOT NULL,
    salary Float not NULL,
    CONSTRAINT PRIMARY PRIMARY KEY (id)
);
-- start the id from 100
ALTER TABLE Employee AUTO_INCREMENT = 100;

CREATE TABLE expenses(
    id INT AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    bond float ,
    Amount float,
    CONSTRAINT PRIMARY PRIMARY KEY (id)

);
CREATE TABLE customer(
    name varchar(255) NOT NULL,
    national_ID varchar(255) NOT NULL,
    phone_number varchar(255) NOT NULL,
    PRIMARY KEY (national_ID)
);

CREATE TABLE creditCustomer(
    id INT NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    customer_NID varchar(255) NOT NULL,
    bond float ,
    Amount float,
    CONSTRAINT PRIMARY PRIMARY KEY (id),
    CONSTRAINT fk_customer_nid FOREIGN KEY (customer_NID) REFERENCES customer(national_ID)
);
CREATE TABLE statement(
    name varchar(255) not null,
    Primary key(name)
);
CREATE TABLE CashMovement(
    id INT NOT NULL AUTO_INCREMENT,
    type ENUM('Receipts', 'payments') NOT NULL,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    bond float ,
    Amount float,
    PRIMARY KEY (id)
);
CREATE TABLE CM_has_S(
    id_cm INT NOT NULL,
    name_S varchar(255) not null,
    FOREIGN KEY (id_cm) REFERENCES CashMovement(id),
    FOREIGN KEY (name_S) REFERENCES statement(name)
);

CREATE TABLE dailyPumpshift(
    id INT NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    pumpNumber INT NOT NULL,
    petrolType Varchar(255) NOT NULL,
    start_code Float NOT NULL,
    end_code float NOt NULL,
    primary key (id)
);
CREATE VIEW dailyPumpshift_liter AS
SELECT 
    id,
    date,
    pumpNumber,
    petrolType,
    start_code,
    end_code,
    (start_code - end_code) AS total_liter
FROM 
    dailyPumpshift;

CREATE TABLE loginHistory(
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    time TIME NOT NULL,
    softwareType VARCHAR(255) NOT NULL,
    primary key (date)
);
CREATE TABLE UserAccount (
    UserName VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Role VARCHAR(255) NOT NULL,
    PRIMARY KEY (UserName)
);
--------------------------------------------
CREATE TABLE userA_has_loginHistory (
    UserName VARCHAR(255),
    Date_login DATE
    FOREIGN KEY (UserName) REFERENCES UserAccount(UserName)
    FOREIGN KEY (Date_login) REFERENCES loginHistory(Date)

);
CREATE TABLE UserA_Has_SActivity (
    UserName VARCHAR(255),
    Date_systemA DATE
    FOREIGN KEY (UserName) REFERENCES UserAccount(UserName)
    FOREIGN KEY (Date_SystemA) REFERENCES SystemActivity(Date)
);
CREATE TABLE SystemActivity (
    Date DATE,
    ModDate DATE,
    time TIME NOT NULL,
    Activity VARCHAR(255) NOT NULL,
    softwareType VARCHAR(255) NOT NULL,
    PRIMARY KEY (Date)
);
CREATE TABLE Oil (
  id INT PRIMARY KEY AUTO_INCREMENT,
  OilName VARCHAR(255) NOT NULL,
  price float NOT NULL
);
CREATE TABLE oilshift(
    Date DATE,
    StartTermBalance float,
    endTermBalance float,
    inbound VARCHAR(255),
    sold INT,
    price float,
    oilname VARCHAR(255) NOT NULL,
    FOREIGN KEY (oilname) REFERENCES Oil(OilName)
);
CREATE TABLE OilStorage(
    Date DATE,
    beginingBalance float,
    endingBalance float,
    inboundtowarehouse VARCHAR(255),
    oilname VARCHAR(255) NOT NULL,
    FOREIGN KEY (oilname) REFERENCES Oil(OilName)
);
CREATE TABLE coupons(
    ID INT,
    Date DATE,
    petrolType VARCHAR(255),
    Issuer VARCHAR(255),
    category VARCHAR(255),
    price float,
    couponserial VARCHAR(255),
    PRIMARY KEY (ID)
);
CREATE TABLE matchingcoupons(
    Date DATE,
    Quantity INT,
    petrolType VARCHAR(255),
    issuer VARCHAR(255),
    category VARCHAR(255),
    coupon_ID INT,
    FOREIGN KEY (coupon_ID) REFERENCES coupons(ID)
);
CREATE VIEW totalprofit_view AS
SELECT 
    StartTermBalance,
    endTermBalance,
    inbound,
    sold,
    price,
    oilname
    (StartTermBalance - endTermBalance) AS total_profit
FROM 
    oilshift;