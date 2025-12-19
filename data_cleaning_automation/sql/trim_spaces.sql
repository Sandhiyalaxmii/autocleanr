-- trim spaces SQL script

UPDATE uploaded_data
SET
    column_name = TRIM(column_name);
