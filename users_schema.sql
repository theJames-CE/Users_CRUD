INSERT INTO users (first_name, last_name, email)
VALUES ("James", "Williams", "jbrandonw88@gmail.com"),
("Shakira", "Sampson", "s_sampson95@gmail.com"),
("Sara", "Amato-Williams", "samato89@gmail.com");

SELECT * FROM users;

SELECT * FROM users
WHERE email = 'jbrandonw88@gmail.com';

SELECT * FROM users
WHERE id = 3;

UPDATE users SET last_name = "Pancakes"
WHERE users.id = 3;

DELETE FROM users
WHERE users.id = 2;

SELECT * FROM users
ORDER BY first_name;

SELECT * FROM users
ORDER BY first_name DESC;