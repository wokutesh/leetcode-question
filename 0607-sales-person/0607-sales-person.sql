# Write your MySQL query statement below
select sp.name
from SalesPerson as sp
where sp.sales_id not in(select ord.sales_id
from Orders as ord
inner join Company as co
on ord.com_id=co.com_id
where co.name ='RED'
)