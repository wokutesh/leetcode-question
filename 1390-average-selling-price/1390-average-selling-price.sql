select p.product_id, Round(IFNULL(sum(p.price*s.units)/ sum(s.units),0), 2) as average_price
from Prices as p LEFT join UnitsSold as s
ON p.product_id = s.product_id
and s.purchase_date between p.start_date and  p.end_date
group by p.product_id;
