CREATE TABLE entry (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_num INT NOT NULL,
    timestamp DATETIME NOT NULL,
    UNIQUE (student_num, timestamp)
);
