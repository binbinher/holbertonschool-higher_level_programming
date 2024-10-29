-- it lists all records with score >= 10 in second table
-- order by score decendent
SELECT score, name
FROM second_table 
WHERE score >= 10
ORDER BY score DESC;
