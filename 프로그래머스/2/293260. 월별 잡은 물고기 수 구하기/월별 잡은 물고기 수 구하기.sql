SELECT COUNT(*) AS FISH_COUNT, MONTH(TIME) AS MONTH
FROM FISH_INFO
GROUP BY MONTH
HAVING FISH_COUNT > 0
ORDER BY MONTH