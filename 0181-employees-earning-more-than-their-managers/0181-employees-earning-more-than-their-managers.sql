# Write your MySQL query statement below
select e2.name as Employee
from Employee as e2
where e2.salary >(select e1.salary from Employee as e1 where e1.id=e2.managerId)