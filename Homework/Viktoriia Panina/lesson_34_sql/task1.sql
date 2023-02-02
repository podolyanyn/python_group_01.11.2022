select first_name, last_name, employees.department_id, department.department_name
from employees
join department
on employees.department_id = department.department_id

select first_name, last_name, d.department_name, l.state_province, l.city
from employees
join department d on employees.department_id = d.department_id
join locations l on d.location_id = l.location_id

select first_name, last_name, d.department_id, d.department_name
from employees
join department d on employees.department_id = d.department_id
where d.department_id = 40 or d.department_id = 80

select first_name, last_name, department.department_id, department.department_name
from employees
right join department
on employees.department_id = department.department_id

select e1.first_name as 'employee', e2.first_name as 'manager'
from employees e1
join employees e2 on e1.employee_id = e2.manager_id

select ("first_name" || " " || "last_name") as 'Full name', jobs.job_title as "Job title", jobs.max_salary-employees.salary as 'Salary difference'
from employees
join jobs on employees.job_id = jobs.job_id

select job_title as "Job title", (min_salary+jobs.max_salary)/2 as "Avarage salary"
from jobs

select ("first_name" || " " || "last_name") as 'Full name', salary, l.city
from employees
join department d on employees.department_id = d.department_id
join locations l on d.location_id = l.location_id
where l.city = 'London'


select d1.department_name, coalesce(c,0)
from department as d1
left join (
select d.department_name, count(*) c
from employees e
join department d on e.department_id = d.department_id
group by department_name) d2
on d1.department_name =  d2.department_name




