
    
    SELECT B.PRODUCT_CODE, (A.TOTAL_NUM * PRICE) AS SALES
FROM (SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS TOTAL_NUM
     FROM OFFLINE_SALE
     GROUP BY PRODUCT_ID) A INNER JOIN PRODUCT B
ON A.PRODUCT_ID = B.PRODUCT_ID order by SALES desc, B.PRODUCT_CODE asc