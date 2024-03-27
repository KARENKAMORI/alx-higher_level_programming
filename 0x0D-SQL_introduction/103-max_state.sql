-- Displays each state's max temp (ordered by State name).

SELECT `state`, MAX(`value`) as `max_temp` FROM `temperatures` GROUP BY `state`;
