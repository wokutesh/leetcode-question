# Write your MySQL query statement below
select id ,movie,description ,rating
 from Cinema
 where MOD(id, 2) = 1 AND description != 'boring'
order by rating desc