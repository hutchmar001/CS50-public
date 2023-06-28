SELECT person_id FROM movies
INNER JOIN person_id ON directors.person_id = movies.id
INNER JOIN rating ON ratings.movie_id = movies.id
WHERE rating >= "9.0";