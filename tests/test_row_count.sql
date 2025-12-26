SELECT 1
FROM (
    SELECT
        (SELECT COUNT(*) FROM uploaded_data) AS raw_rows,
        (SELECT COUNT(*) FROM clean_table) AS clean_rows
) t
WHERE clean_rows > raw_rows;

