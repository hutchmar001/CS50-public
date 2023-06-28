SELECT person_id FROM stars
INNER JOIN people ON people.id = stars.person_id
WHERE