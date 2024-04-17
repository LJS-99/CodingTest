SELECT COUNT(ID) AS FISH_COUNT, FISH_NAME
FROM FISH_INFO JOIN FISH_NAME_INFO USING (FISH_TYPE)
GROUP BY FISH_NAME
ORDER BY FISH_COUNT DESC