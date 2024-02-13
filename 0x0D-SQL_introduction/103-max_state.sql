SELECT State, MAX(Temperature) AS max_temperature
From temperatures
GROUP BY State
ORDER BY State;
