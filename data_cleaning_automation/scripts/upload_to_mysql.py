# upload file to MySQL (CORRECT VERSION)

import pandas as pd
import mysql.connector
import json
import os

# Base directory (engine)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSV_PATH = os.path.join(BASE_DIR, "data", "sample.csv")
CONFIG_PATH = os.path.join(BASE_DIR, "config", "db_config.json")

with open(CONFIG_PATH) as f:
    config = json.load(f)


df = pd.read_csv(CSV_PATH)

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS uploaded_data;")


columns = ", ".join([f"`{col}` TEXT" for col in df.columns])
cursor.execute(f"CREATE TABLE uploaded_data ({columns});")


for _, row in df.iterrows():
    values = "', '".join([str(x) for x in row.values])
    cursor.execute(f"INSERT INTO uploaded_data VALUES ('{values}')")

conn.commit()

cursor.execute("DROP TABLE IF EXISTS clean_table;")

cursor.execute("""
CREATE TABLE clean_table AS
SELECT *
FROM uploaded_data;
""")

conn.commit()

cursor.close()
conn.close()

print("✅ Dataset uploaded and clean_table created successfully")
