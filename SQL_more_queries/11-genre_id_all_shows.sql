-- this script lists all shows contained in the database hbtn_0d_tvshows.
-- record should display tv_shows.title and tv_show_genres.genre_id
-- sored in ascending order by both
-- if it doesnt have a genre,display NULL

SELECT
    tv_shows.title,
		tv_show_genres.genre_id
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_show.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
		tv_show_genres.genre_id ASC;
