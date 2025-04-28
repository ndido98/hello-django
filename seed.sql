CREATE DATABASE IF NOT EXISTS hello;

USE hello;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS poll (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS poll_option (
    id INT AUTO_INCREMENT PRIMARY KEY,
    poll_id INT NOT NULL,
    option_text VARCHAR(255) NOT NULL,

    FOREIGN KEY (poll_id) REFERENCES poll(id)
);

CREATE TABLE IF NOT EXISTS vote (
    poll_id INT NOT NULL,
    option_id INT NOT NULL,
    user_id INT NOT NULL,

    PRIMARY KEY (poll_id, user_id),
    FOREIGN KEY (poll_id) REFERENCES poll(id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (option_id) REFERENCES poll_option(id)
);