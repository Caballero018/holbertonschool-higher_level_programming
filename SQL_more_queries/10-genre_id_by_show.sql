-- Import the database dump from hbtn_0d_tvshows to your MySQL server.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tvshows INNER JOIN tv_show_genres ON tvshows.id = tv_show_genres.id;