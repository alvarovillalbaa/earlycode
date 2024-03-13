/* we will insert the following on the localhost server database to create table with columns: */
CREATE TABLE users (
    usersId int(100) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    usersName varchar
(256) NOT NULL,
    usersEmail varchar
(256) NOT NULL,
    usersUid varchar
(256) NOT NULL,
    usersPwd varchar
(256) NOT NULL
);

INSERT INTO users
    (usersName, usersEmail, usersUid, usersPwd)
VALUES
    ('Alvaro', 'alvaro@gmail.com', 'Administrator', 'test123');