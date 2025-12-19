import mysql.connector
import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "db_config.json")


with open(CONFIG_PATH) as f:
    config = json.load(f)

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

TABLE_NAME = "uploaded_data"


cursor.execute("""
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = %s
      AND TABLE_SCHEMA = %s
""", (TABLE_NAME, config["database"]))

columns = [row[0] for row in cursor.fetchall()]

trim_clauses = [f"`{col}` = TRIM(`{col}`)" for col in columns]

trim_query = f"""
UPDATE {TABLE_NAME}
SET {", ".join(trim_clauses)};
"""

cursor.execute(trim_query)
conn.commit()
print("Trimming completed")


null_clauses = [f"`{col}` = NULLIF(`{col}`, '')" for col in columns]

null_query = f"""
UPDATE {TABLE_NAME}
SET {", ".join(null_clauses)};
"""

cursor.execute(null_query)
conn.commit()
print("Empty strings converted to NULL")

cursor.close()
conn.close()

print("Cleaning step completed successfully")

