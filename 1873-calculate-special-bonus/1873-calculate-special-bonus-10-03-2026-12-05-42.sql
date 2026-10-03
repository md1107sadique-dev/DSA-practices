SELECT employee_id,
CASE
    WHEN name NOT LIKE 'M%' and employee_id % 2 <> 0 Then salary
    ELSE 0
END AS bonus
FROM Employees
ORDER BY employee_id ASC
