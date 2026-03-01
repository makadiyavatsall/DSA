CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  -- Declare a variable to hold the offset (N-1)
  DECLARE M INT;
  SET M = N - 1;
  
  RETURN (
      -- Write your MySQL query statement below.
      SELECT DISTINCT salary 
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET M
  );
END