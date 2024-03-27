-- Lists the number of records with the same score in second_table.
-- display the score and the records number
-- for score with the label number, ordered by score.

SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
