SELECT E.first_name, E.last_name, E.department_id, D.depart_name FROM employees as E INNER JOIN departments as D ON E.department_id = D.department_id;
SELECT E.first_name, E.last_name, D.depart_name,  L.city, L.state_province FROM employees  as E INNER JOIN departments as D ON E.department_id = D.department_id INNER JOIN locations as L on D.location_id = L.location_id;
SELECT E.first_name, E.last_name, D.department_id, D.depart_name FROM employees  as E INNER JOIN departments as D ON E.department_id = D.department_id where D.department_id = 40 or D.department_id = 80;
SELECT department_id, depart_name FROM departments;
SELECT E.first_name as 'Employee Name', M.first_name as 'Manager_Name' FROM employees as E INNER  JOIN employees as M on E.manager_id = M.employee_id;
SELECT J.job_title, (E.first_name || ' ' || E.last_name) as 'Full Name', J.max_salary - E.salary as 'Max Salary Delta' FROM employees as E INNER JOIN jobs as J on E.job_id = J.job_id;
SELECT J.job_title as 'Job Title', avg(E.salary) as 'Average Salary' FROM employees as E INNER JOIN jobs as J on E.job_id = J.job_id GROUP BY E.job_id ORDER BY MAX(E.salary) DESC;
SELECT (E.first_name || ' ' || E.last_name) as 'Full Name', E.Salary FROM employees  as  E INNER JOIN departments as  D on E.department_id =  D.department_id  INNER JOIN locations as L  on D.location_id = L.location_id WHERE L.city = 'London';
SELECT D.depart_name as  'Department Name', count(E.employee_id)  as 'No. of employees' FROM employees as E INNER JOIN departments as D on E.department_id =  D.department_id GROUP BY E.department_id