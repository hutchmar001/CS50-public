SELECT * FROM stars
INNER JOIN people ON people.id = stars.person_id
INNER JOIN movies ON movies.id = stars.movie_id
WHERE name = "Johnny Depp" OR name = "Helena Bonham Carter";