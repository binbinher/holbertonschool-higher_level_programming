-- this script creates database hbtn_0d_usa and table cities
-- cities id INT unique auto generated, not null and primary key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- Create the states table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
		name VARCHAR(256) NOT NULL,
		PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
		state_id INT NOT NULL,
		name VARCHAR(256) NOT NULL,
		PRIMARY KEY (id),
		FOREIGN KEY (state_id) REFERENCES states(id)
);
