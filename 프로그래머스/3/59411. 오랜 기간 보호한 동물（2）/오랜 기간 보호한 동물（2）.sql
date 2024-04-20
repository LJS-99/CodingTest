SELECT
    ANIMAL_ID, 
    B.NAME
FROM
    ANIMAL_INS A JOIN ANIMAL_OUTS B USING (ANIMAL_ID)
ORDER BY
    TIMESTAMPDIFF(MINUTE, A.DATETIME, B.DATETIME) DESC
LIMIT
    2