# Write your MySQL query statement below
SELECT employee_id 
FROM (
    SELECT employee_id FROM Employees
    UNION 
    SELECT employee_id FROM Salaries
) AS all_ids
WHERE employee_id NOT IN (SELECT employee_id FROM Employees 
                          INNER JOIN Salaries USING (employee_id))
ORDER BY employee_id;
