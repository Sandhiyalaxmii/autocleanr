-- remove duplicates SQL script
-- Remove duplicate rows using a temporary table

CREATE TABLE uploaded_data_dedup AS
SELECT DISTINCT * FROM uploaded_data;

DROP TABLE uploaded_data;

RENAME TABLE uploaded_data_dedup TO uploaded_data;


