CREATE DATABASE pollution_dbms;

USE pollution_dbms;

CREATE TABLE pollution_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    aqi FLOAT,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO pollution_data(city, aqi, temperature, humidity, wind_speed) VALUES
('Delhi', 28.7, 47.1, 20, 150),
('Hyderabad', 22.7, 387.1, 220, 180);

select * from pollution_data;