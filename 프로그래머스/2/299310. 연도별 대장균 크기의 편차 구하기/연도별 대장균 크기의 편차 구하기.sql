SELECT SUB.YEAR, (SUB.MAX_SIZE - SUB.SIZE_OF_COLONY) AS YEAR_DEV, SUB.ID
FROM(
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, 
    SIZE_OF_COLONY,
    MAX(SIZE_OF_COLONY) OVER (PARTITION BY YEAR(DIFFERENTIATION_DATE)) AS MAX_SIZE, ID FROM ECOLI_DATA) AS SUB
ORDER BY YEAR, YEAR_DEV