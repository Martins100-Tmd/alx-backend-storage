-- Task 1 file
-- creates table 'users' if not exist
-- table fields; id, name, email, country
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL,
	UNIQUE(email),
	PRIMARY KEY(id)
	);
