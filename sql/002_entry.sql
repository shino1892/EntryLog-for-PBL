CREATE TABLE entry (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    timestamp DATETIME NOT NULL,
    record_date DATE AS (DATE(timestamp)) STORED,
    UNIQUE (user_id, record_date)
);
