-- Query to list records of the second_table with
-- non-empty name and order by descending scores
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
