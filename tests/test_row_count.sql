SELECT
    'Row count increased after cleaning' AS error_message,
    raw_rows,
    clean_rows
FROM (
    SELECT
        (SELECT COUNT(*) FROM raw_table)  AS raw_rows,
        (SELECT COUNT(*) FROM clean_table) AS clean_rows
) counts
WHERE clean_rows > raw_rows;
