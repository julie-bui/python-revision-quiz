CREATE DATABASE IF NOT EXISTS logins;
USE logins;

CREATE TABLE IF NOT EXISTS logins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

INSERT INTO logins (firstname, lastname, username, password) VALUES
('Alice', 'Brown', 'alice123', 'pass123'),
('Bob', 'Smith', 'bob123', 'mypassword'),
('Test', 'User', 'test', '1234');   
