CREATE TABLE anime_list (
    id INTEGER PRIMARY KEY,
    title UNIQUE,
    rating INTEGER NOT NULL
);

ALTER TABLE anime_list
RENAME TO  movie_list;

ALTER TABLE movie_list
ADD COLUMN year INTEGER;

INSERT INTO movie_list (id, title, rating, year)
VALUES (1, 'The Shawshank Redemption', 1, 1994);

INSERT INTO movie_list (id, title, rating, year)
VALUES (2, 'The Godfather', 2, 1972);

INSERT INTO movie_list (id, title, rating, year)
VALUES (3, 'The Dark Knight', 3, 2008);

INSERT INTO movie_list (id, title, rating, year)
VALUES (4, '12 Angry Men', 4, 1957);

INSERT INTO movie_list (id, title, rating, year)
VALUES (5, 'Pulp Fiction', 5, 1994);

UPDATE movie_list
SET title = "Home Alone"
WHERE rating = 5;

UPDATE movie_list
SET year = 1990
WHERE title = "Home Alone";

DELETE FROM movie_list
WHERE rating = 5;
