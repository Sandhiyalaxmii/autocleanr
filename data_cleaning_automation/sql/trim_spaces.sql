-- trim spaces SQL script
-- Remove leading and trailing spaces from all text columns
-- (Columns are dynamically discovered in Python)

UPDATE uploaded_data
SET
    column_name = TRIM(column_name);
