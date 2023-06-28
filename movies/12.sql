SELECT title FROM stars
INNER JOIN people ON people.id = stars.person_id
INNER JOIN movies ON movies.id = stars.movie_id
WHERE EXISTS (SELECT "Helena Bonham Carter" FROM name )


IN (name) AND "Johnny Depp" IN (name);