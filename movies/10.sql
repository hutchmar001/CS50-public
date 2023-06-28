SELECT person_id FROM movies
INNER JOIN directors ON directors.movie_id = movies.id
INNER JOIN ratings ON ratings.movie_id = movies.id
WHERE rating >= "9.0";