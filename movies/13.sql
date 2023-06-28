SELECT name FROM stars
INNER JOIN people ON people.id = stars.person_id
INNER JOIN movies ON movies.id = stars.movie_id
WHERE title NOT IN
(
SELECT title FROM stars
INNER JOIN people ON people.id = stars.person_id
INNER JOIN movies ON movies.id = stars.movie_id
WHERE "Kevin Bacon" IN (name) AND birth = "1958"
)
LIMIT 5;