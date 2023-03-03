select first_name, last_name, employees.department_id, depart_name
from employees
join departments
    on employees.department_id = departments.department_id;

select first_name, last_name, depart_name, city, state_province
from employees
join departments
    on employees.department_id = departments.department_id
join locations
    on departments.location_id = locations.location_id;

select first_name, last_name, employees.department_id, depart_name
from employees
join departments
    on employees.department_id = departments.department_id
where employees.department_id = 80 or employees.department_id = 40;

select *
from departments
join employees
where employees.department_id IS NULL;

select e1.first_name as "employees", e2.first_name as "managers"
from employees as e1
inner join employees as e2
    on e1.manager_id = e2.employee_id;


select jobs.job_title as "Job",
       employees.first_name || " " || employees.last_name AS "Full name",
       (jobs.max_salary - employees.salary) as "Difference"
from employees
inner join jobs
    on jobs.job_id = employees.job_id
GROUP BY employees.first_name;

SELECT jobs.job_title, AVG(salary)
FROM employees
inner join jobs
    on jobs.job_id = employees.job_id
GROUP BY employees.job_id;

select employees.first_name || " " || employees.last_name AS "Full name", employees.salary
from employees
join departments
    on employees.department_id = departments.department_id
join locations
    on departments.location_id = locations.location_id
where locations.city is "London";

select departments.depart_name, COUNT(employees.employee_id)as "Number of workers"
from departments
inner join employees
    on departments.department_id = employees.department_id
GROUP BY depart_name;