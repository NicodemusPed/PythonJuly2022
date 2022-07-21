SELECT*FROM users;
INSERT INTO users (first_name, LAST_NAME, EMAIL)
VALUES ("July", "Fun", "jf@email.com"), ("Emily", "Rappaort", "er@email.com"),
("Joe", "Drop", "jd@email.com");
DELETE FROM users WHERE id=5;
SELECT * FROM users ORDER BY first_NAME DESC;
UPDATE users SET LAST_NAME = "Pancakes" WHERE id=6;
SELECT * FROM users WHERE EMAIL='jf@email.com';
SELECT * FROM users WHERE id=6;