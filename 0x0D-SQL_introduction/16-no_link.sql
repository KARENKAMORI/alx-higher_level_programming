-- Lists all records in the current database second_table table.
-- displays the score and the name, ordered by score.

SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
