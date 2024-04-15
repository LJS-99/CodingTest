SELECT ID,
CASE WHEN PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY) > 0.75 THEN 'CRITICAL'
WHEN PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY) > 0.5 THEN 'HIGH'
WHEN PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY) > 0.25 THEN 'MEDIUM'
ELSE 'LOW' END AS 'COLONY_NAME'
FROM ECOLI_DATA
ORDER BY ID;