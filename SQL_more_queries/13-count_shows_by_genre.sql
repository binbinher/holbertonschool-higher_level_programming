-- this script lists all genres and display the number of shows linked to each
-- TVshow genre, number of shows linked to this genre should be displayed
-- first column must be called genre, second is number_of_shows
-- sorted in descentding order by number of shows

SELECT tv_genres.names AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
