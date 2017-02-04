INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
VALUES ('Obi', 'Wan', 'Jedi', NOW(), NOW());


SELECT * from friends;

DELETE FROM friends
WHERE id = 10;