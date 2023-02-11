SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;

SELECT DISTINCT department_id as "Department ID"
from employees;

SELECT *
FROM employees
ORDER BY first_name DESC;

SELECT first_name AS "First Name", last_name AS "Last Name",
       salary as "Income", salary * 0.12 AS "PF"
from employees;

SELECT MIN(salary), MAX(salary)
from employees;

SELECT salary + (employees.salary*employees.commission_pct) as "Monthly salary"
FROM employees;