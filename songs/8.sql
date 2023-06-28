SELECT name FROM songs
FROM songs
INNER JOIN artists ON songs.artist_id = artists.id
WHERE artists.name LIKE 