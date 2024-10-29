-- it lists all records of second_table
-- dont list row without a name value 
-- records listd by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
