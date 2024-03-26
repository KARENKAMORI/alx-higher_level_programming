-- Creates first_table table in the current database,
-- if the first_table table already exists, do nothing.

CREATE TABLE IF NOT EXISTS `first_table` (
	`id` INT,
	`name` VARCHAR(256)
);
