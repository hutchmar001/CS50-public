SELECT name FROM stars
INNER JOIN people ON people.id = stars.person_id
INNER JOIN movies ON movies.id = stars.movie_id
INNER JOIN ratings ON movies.id = ratings.movie_id
WHERE name = "Chadwick Boseman"
ORDER BY
LIMIT 5;