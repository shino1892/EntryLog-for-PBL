CREATE TABLE entry (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_num INT NOT NULL,
    timestamp DATETIME NOT NULL,
    record_date DATE AS (DATE(timestamp)) STORED,
    UNIQUE (student_num, record_date)
);
