SELECT
    email,
    COUNT(*) AS occurrences
FROM clean_table
GROUP BY email
HAVING COUNT(*) > 1;
