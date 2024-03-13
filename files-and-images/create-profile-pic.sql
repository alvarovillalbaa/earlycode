CREATE TABLE users (
    user int
(100) PRIMARY KEY AUTO_INCREMENT NOT NULL,
userFullName varchar
(256) NOT NULL,
userName varchar
(255) NOT NULL,
userEmail varchar
(255) NOT NULL,
userPwd varchar
(255) NOT NULL
)

CREATE TABLE profileimg (
    user int
(100) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    userId int
(100) NOT NULL,
    status int
(100) NOT NULL
)