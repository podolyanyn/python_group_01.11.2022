-- Task 1 Create a table
-- Create a table of your choice inside the sample SQLite database,
CREATE TABLE city(
    capital varchar,
    postcode varchar(5)
    );

-- rename it,
ALTER TABLE city
RENAME TO towns;

ALTER TABLE towns
RENAME COLUMN capital to main_town;

-- and add a new column.
ALTER TABLE towns
ADD currency varchar(3);

-- Insert a couple rows inside your table.
INSERT INTO towns
VALUES ('Kyiv', '01001', 'UAH');

INSERT INTO towns (main_town, postcode, currency) VALUES ('Dnipro', '49000', 'UAH');


-- Also, perform UPDATE
UPDATE towns
SET postcode = '01033'
WHERE main_town = 'Kyiv';

UPDATE towns
SET currency = 'грн';


-- and DELETE statements on inserted rows.
DELETE FROM towns WHERE main_town='Dnipro';

-- As a solution to this task, create a file named: les33_task1.sql, with all the SQL statements you have used to accomplish this task