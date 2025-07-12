CREATE DATABASE room_booking;

USE room_booking;

-- table->category

CREATE TABLE Category(
ID INT PRIMARY KEY AUTO_INCREMENT,
Status ENUM('active','inactive') DEFAULT 'active',
created_by INT,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
Updated_by INT,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
catogory_name VARCHAR(30) NOT NULL
);


-- Table: Rooms
CREATE TABLE Rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    category_id INT,
    room_name VARCHAR(50) NOT NULL,
    status ENUM('active', 'inactive') DEFAULT 'active',
    checkin_date DATE,
    checkout_date DATE,
    created_by INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Category(id)
);

-- Table: Bookings
CREATE TABLE Bookings (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    room_id INT,
    name VARCHAR(30),
    phone_no BIGINT,
    email VARCHAR(50),
    gender VARCHAR(10),
    state VARCHAR(30),
    city VARCHAR(30),
    guests INT,
    id_proof VARCHAR(30),
    checkin_date DATE,
    checkout_date DATE,
    status ENUM('active', 'inactive'),
    created_by INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_by INT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

ALTER TABLE Bookings ADD COLUMN id_number VARCHAR(30) AFTER id_proof;
ALTER TABLE Bookings ADD COLUMN room_name VARCHAR(50) AFTER ID;

ALTER TABLE Bookings DROP COLUMN room_id;


SELECT * FROM Bookings;





