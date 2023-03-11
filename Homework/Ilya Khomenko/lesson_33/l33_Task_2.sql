SELECT first_name as 'First Name', last_name as 'Last Name' FROM employees;
SELECT DISTINCT department_id FROM employees;
SELECT * FROM employees ORDER BY first_name DESC;
SELECT first_name, last_name, salary, salary * 0.12 as 'PF' FROM employees;
SELECT max(salary), min(salary) FROM employees;
SELECT employee_id as 'ID', round((salary / 12), 2) as 'Monthly Salary' FROM employees;