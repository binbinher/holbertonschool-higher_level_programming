-- this script lists all genres and display the number of shows linked to each
-- TVshow genre, number of shows linked to this genre should be displayed
-- sorted in descentding order by number of shows

SELECT tv_genres.names AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
-- Join the tv_genres table with the tv_show_genres table
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
-- Only include genres that have at least one show
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
