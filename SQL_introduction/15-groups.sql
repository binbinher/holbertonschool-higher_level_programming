-- it lists the number of records with the same score in the table
-- it displays the score and the number of records
-- sorted by the number of records descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESCL;
