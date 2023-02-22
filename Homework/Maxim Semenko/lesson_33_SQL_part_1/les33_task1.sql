CREATE TABLE Sales_Department (employee_id int, employee_full_name varchar(200));
ALTER TABLE Sales_Department RENAME TO Sales_Dept;
ALTER TABLE Sales_Dept ADD salary varchar(200);
INSERT INTO Sales_Dept VALUES (1, 'Petro Shevchenko', 4000);
INSERT INTO Sales_Dept VALUES (2, 'Vika Shevchenko', 10000);
INSERT INTO Sales_Dept VALUES (3, 'Mykola Shevchenko', 11000);
SELECT * FROM Sales_Dept ORDER BY salary DESC LIMIT 10;
DELETE FROM Sales_Dept WHERE salary < 3000;
UPDATE Sales_Dept SET salary = 'Over 9000' WHERE salary > 9000;