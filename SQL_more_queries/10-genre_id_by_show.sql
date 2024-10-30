-- this script lists all shows contained in hbtn_0d_tvshows that has at least one genre linked

SELECT
    tv_shows.title,
		tv_show_genres.genre_id
FROM
    tv_shows,
		tv_show_genres
JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
		tv_show_genres.genre.id ASC;
