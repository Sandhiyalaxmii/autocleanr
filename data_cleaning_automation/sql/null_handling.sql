-- Convert empty strings to NULL values
UPDATE uploaded_data
SET
    column_name = NULLIF(column_name, '');
