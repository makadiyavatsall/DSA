# Write your MySQL query statement below
SELECT 
    email as Email
from Person 
Group by email
having count(*) >1