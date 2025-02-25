# Write your MySQL query statement below
select * from products
where description regexp 'SN[0-9]{4}-[0-9]{4}' AND description NOT REGEXP 'SN[0-9]{4}-[0-9]{5,}'
order by product_id