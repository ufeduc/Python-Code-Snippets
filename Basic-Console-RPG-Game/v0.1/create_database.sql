CREATE DATABASE users;
USE users;
CREATE TABLE accounts(id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(10),password VARCHAR(10),date_of_create DATETIME);
CREATE TABLE characters(id INT AUTO_INCREMENT PRIMARY KEY,health INT,mana INT,attack INT,balance INT,experience INT,level INT,job VARCHAR(100),account_id INT,FOREIGN KEY(account_id) REFERENCES accounts(id));
