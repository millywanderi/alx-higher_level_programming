-- displays the max temperature of each state
SELECT STATE
MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state asc;
