# Write your MySQL query statement below
SELECT 
    id,
    movie,
    description,
    rating
from cinema
where id % 2 = 1 and description != 'boring'
order by rating desc