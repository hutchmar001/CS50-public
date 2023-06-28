SELECT name FROM movies
INNER JOIN directors ON directors.movie_id = movies.id
INNER JOIN ratings ON ratings.movie_id = movies.id
INNER JOIN people ON people.id = directors.person_id
WHERE rating >= "9.0";