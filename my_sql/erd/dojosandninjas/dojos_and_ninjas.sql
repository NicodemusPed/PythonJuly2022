SELECT * FROM dojos;
SELECT * FROM ninjas;
INSERT INTO dojos (name) VALUES ('Top'), ('middle'), ('bottom');
SET SQL_SAFE_UPDATES = 0;
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id)
Values ("Dave", "Brayant", "35", NOW(), NOW(), 4), ("Will", "Groper", "12", NOW(), NOW(), 4), ("Susie", "herald","22", NOW(), NOW(), 4);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id)
Values ("Reggy", "Wilson", "55", NOW(), NOW(), 5), ("Brenda", "Williams", "8", NOW(), NOW(), 5), ("Jeff", "George","39", NOW(), NOW(), 5);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id)
Values ("Bev", "War", "66", NOW(), NOW(), 6), ("Kim", "Will", "18", NOW(), NOW(), 6), ("Kyle", "Pops","39", NOW(), NOW(), 6);

SELECT * FROM ninjas WHERE dojos_id=4;
SELECT * FROM ninjas WHERE dojos_id=5;
SELECT * FROM ninjas WHERE dojos_id=6;
