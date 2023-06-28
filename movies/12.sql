SELECT title FROM stars
INNER JOIN people ON people.id = stars.person_id
INNER JOIN movies ON movies.id = stars.movie_id
WHERE "Helena Bonham Carter" IN (name) AND "Johnny Depp" IN (name);