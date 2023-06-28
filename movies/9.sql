SELECT name FROM stars
INNER JOIN people ON people.id = stars.person_id
INNER JOIN movies ON movies.id = stars.movie_id
WHERE year = "2004"
ORDER BY birth ASC;