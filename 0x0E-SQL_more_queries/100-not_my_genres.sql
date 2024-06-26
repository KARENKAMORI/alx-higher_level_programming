-- a script that uses the hbtn_0d_tvshows database to list all
-- genres not linked to the show Dexter.

  SELECT tv_genres.name FROM tv_genres WHERE tv_genres.name NOT IN (
      SELECT g.name
        FROM (tv_shows s JOIN tv_show_genres sg ON s.id = sg.show_id)
        JOIN tv_genres g ON sg.genre_id = g.id
       WHERE s.title = "Dexter")
ORDER BY tv_genres.name;
