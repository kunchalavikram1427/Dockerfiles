CREATE DATABASE IF NOT EXISTS todo;
USE todo;
CREATE TABLE todo (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(100), complete BOOLEAN);