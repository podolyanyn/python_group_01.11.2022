-- Joins
--
-- Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)
--
-- As a solution to HW, create a file named: task1.sql with all SQL queries:
--
--
-- 1) write a query in SQL to display the first name, last name, department number, and department name for each employee
SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
FROM employees
LEFT JOIN department
ON employees.department_id = department.department_id
ORDER BY employees.department_id;


-- 2) write a query in SQL to display the first and last name, department, city, and state province for each employee
SELECT employees.first_name, employees.last_name, department.department_name, locations.city, locations.state_province
FROM employees
LEFT JOIN department
ON employees.department_id = department.department_id
LEFT JOIN locations
ON department.location_id = locations.location_id;


-- 3) write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
FROM employees
JOIN department
ON employees.department_id = department.department_id
WHERE employees.department_id = 80 OR employees.department_id = 40
ORDER BY employees.department_id;

-- 4) write a query in SQL to display all departments including those where does not have any employee
SELECT d.department_id, d.department_name, COUNT(e.employee_id) AS employees_number
FROM department AS d
LEFT JOIN employees AS e
ON d.department_id = e.department_id
GROUP BY d.department_id
ORDER BY employees_number DESC;

-- 5) write a query in SQL to display the first name of all employees including the first name of their manager
SELECT e.employee_id, e.first_name AS employee_name, managers.first_name AS manager_name
FROM employees AS e, employees AS managers
WHERE e.manager_id = managers.employee_id;


-- 6) write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT (e.first_name || ' '|| e.last_name) AS full_name, (jobs.max_salary - e.salary) AS salary_gap
FROM employees as e
JOIN jobs
ON e.job_id = jobs.job_id;

-- 7) write a query in SQL to display the job title and the average salary of employees
SELECT jobs.job_title, jobs.max_salary, AVG(e.salary) AS salary_average
FROM jobs
JOIN employees as e
ON jobs.job_id = e.job_id
GROUP BY e.job_id;

-- 8) write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
SELECT (e.first_name || ' '|| e.last_name) AS full_name, e.salary, d.location_id
FROM employees AS e
LEFT JOIN department AS d
ON e.department_id = d.department_id
LEFT JOIN locations as l
ON d.location_id = l.location_id
WHERE l.city = 'London';


-- 9) write a query in SQL to display the department name and the number of employees in each department
SELECT d.department_name, COUNT(e.employee_id)
FROM department AS d
LEFT JOIN employees AS e
ON d.department_id = e.department_id
GROUP BY d.department_id;