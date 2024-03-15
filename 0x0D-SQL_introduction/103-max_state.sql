-- Displays the max temperature of each state, ordered by state name.
SELECT state, MAX(value) AS max_temp
From temperatures
GROUP BY state
ORDER BY state;
