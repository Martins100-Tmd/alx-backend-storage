-- Task 0's file
-- Creating a table if it doesn't exist
-- Table field; id, name, email
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL,
	name VARCHAR(255),
	UNIQUE(email),
	PRIMARY KEY(id)
	);
