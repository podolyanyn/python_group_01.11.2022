select first_name as 'Fisrt Name', last_name as 'Last Name'
from employees

select distinct department_id
from employees

select *
from employees
order by first_name desc

select first_name, last_name, salary, salary*0.12 as PF
from employees

select min(salary) as 'Min salary',
       max(salary) as 'Max salary'
from employees

select first_name, last_name, round(salary, 2)
from employees

