create table task_1(
    id int primary key,
    first_name text,
    last_name text,
    phone_number int
)
alter table task_1
rename to task1

alter table task1
add email text

insert into task1(id, first_name, last_name, phone_number, email)
VALUES (001, 'Vika', 'Panina', 0631112233, 'vi@test.com')

insert into task1(id, first_name, last_name, phone_number, email)
VALUES (002, 'Daisy', 'Panina', 3807729011, 'dog@test.com')

update task1
set phone_number = 380631047219
where id = 001

delete from task1
where id = 001
