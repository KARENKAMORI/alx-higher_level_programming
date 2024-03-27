-- Lists all records with a score >= 10 of second_table table.
-- display the score and the name, ordered by score.

SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
