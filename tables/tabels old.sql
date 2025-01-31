--
CREATE TABLE petrolprice(
    date TIMESTAMP NOT NULL,
    solarprice float NOT NULL,
    petrol80price float NOT NULL,
    petrol92price float NOT NULL,
    petrol95price float NOT NULL,
    CONSTRAINT PRIMARY KEY (date)
    
);

--
CREATE TABLE dailyPumpshift(
    id INT NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL,
    pumpNumber INT NOT NULL,
    petrolType Varchar(255) NOT NULL,
    start_code Float NOT NULL,
    end_code float NOt NULL,
    primary key (id)
);

--
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

--
CREATE TABLE oil (
  oilName VARCHAR(255) NOT NULL,
  price float,
  primary key (oilName)
 );
 
 --
CREATE TABLE oilshift(
    date TIMESTAMP NOT NULL,
    StartTermBalance float ,
    endTermBalance float ,
    sold INT NOT NULL,
    price float ,
    oilname VARCHAR(255) NOT NULL,
    FOREIGN KEY (oilname) REFERENCES oil(oilName)
);

--
CREATE VIEW totalprofit_view AS
SELECT 
    StartTermBalance,
    endTermBalance,
    inbound,
    sold,
    price,
    oilname,
    (StartTermBalance - endTermBalance) AS total_profit
FROM 
    oilshift;

--
CREATE TABLE OilStorage(
    date TIMESTAMP NOT NULL,
    beginingBalance float,
    endingBalance float,
    inboundtowarehouse VARCHAR(255),
    oilname VARCHAR(255) NOT NULL,
    FOREIGN KEY (oilname) REFERENCES oil(oilName)
);

--
CREATE TABLE expenses(
    id INT NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL,
    bond VARCHAR(255) NOT NULL,
    Amount float  NOT NULL,
    CONSTRAINT PRIMARY KEY (id)
);

--
CREATE TABLE coupons(
    id INT NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL,
    petrolType VARCHAR(255) NOT NULL,
    Issuer VARCHAR(255) NOT NULL,
    category INT NOT NULL,
    price float ,
    total float,
    couponserial VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

--
CREATE TABLE matchingcoupons(
    date TIMESTAMP NOT NULL,
    Quantity INT NOT NULL,
    petrolType VARCHAR(255) NOT NULL,
    issuer VARCHAR(255) NOT NULL,
    category INT NOT NULL,
	total float
);

--
CREATE TABLE customer(
    name varchar(255) not NULL,
    national_ID varchar(255) NOT NULL,
    phone_number varchar(255) NOT NULL,
    PRIMARY KEY (national_ID)
);

--
CREATE TABLE creditCustomer(
    id INT NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL,
    customer_NID varchar(255) NOT NULL,
    bond varchar(255) NOT NULL,
    Amount float,
    CONSTRAINT PRIMARY KEY (id),
    CONSTRAINT fk_customer_nid FOREIGN KEY (customer_NID) REFERENCES customer(national_ID)
);

--
CREATE TABLE statement(
    name varchar(255) not null,
    Primary key(name)
);

--
CREATE TABLE CashMovement(
    id INT NOT NULL AUTO_INCREMENT,
    type ENUM('مقبوضات', 'مدفوعات') NOT NULL,
    date TIMESTAMP NOT NULL,
    bond varchar(255) NOT NULL,
    Amount float,
    PRIMARY KEY (id)
);

--
CREATE TABLE CM_has_S(
    id_cm INT NOT NULL,
    name_S varchar(255) not null,
    FOREIGN KEY (id_cm) REFERENCES CashMovement(id),
    FOREIGN KEY (name_S) REFERENCES statement(name)
);
    
--
CREATE TABLE Employee(
    id INT AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    nationalID varchar(255) NOT NULL,
    phoneNumber varchar(255) NOT NULL,
    job varchar(255) NOT NULL,
    salary Float not NULL,
    CONSTRAINT PRIMARY KEY (id)
);

-- start the id from 100
ALTER TABLE Employee AUTO_INCREMENT = 100;

--
CREATE TABLE UserAccount (
    UserName VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Role VARCHAR(255) NOT NULL,
    PRIMARY KEY (UserName)
);

--
CREATE TABLE loginHistory(
	id INT AUTO_INCREMENT,
    date TIMESTAMP NOT NULL,
    time TIME NOT NULL,
    softwareType VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);

--
CREATE TABLE userA_has_loginHistory (
    User_Name VARCHAR(255) NOT NULL,
    h_id INT NOT NULL,
    FOREIGN KEY (User_Name) REFERENCES UserAccount(UserName),
    FOREIGN KEY (h_id) REFERENCES loginHistory(id)
);

--
CREATE TABLE SystemActivity (
	id INT AUTO_INCREMENT,
    date TIMESTAMP NOT NULL,
    ModDate TIMESTAMP NOT NULL,
    time TIME NOT NULL,
    Activity VARCHAR(255) NOT NULL,
    softwareType VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);

--
CREATE TABLE UserA_Has_SActivity (
    UserName VARCHAR(255) NOT NULL,
    a_id INT NOT NULL,
    FOREIGN KEY (UserName) REFERENCES UserAccount(UserName),
    FOREIGN KEY (a_id) REFERENCES SystemActivity(id)

);