SELECT
    A.ID, B.FISH_NAME, A.LENGTH
FROM
    FISH_INFO A LEFT JOIN FISH_NAME_INFO B USING (FISH_TYPE)
WHERE
    (FISH_TYPE, LENGTH) IN (SELECT
                                FISH_TYPE, MAX(LENGTH) AS LENGTH
                            FROM
                                FISH_INFO
                            GROUP BY
                                FISH_TYPE)
ORDER BY
    A.ID
    