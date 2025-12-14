# upload file to MySQL

import pandas as pd
import mysql.connector
import json
import os

# Base directory (data_cleaning_automation)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSV_PATH = os.path.join(BASE_DIR, "data", "sample.csv")
CONFIG_PATH = os.path.join(BASE_DIR, "config", "db_config.json")

# Load DB config
with open(CONFIG_PATH) as f:
    config = json.load(f)

# Read CSV
df = pd.read_csv(CSV_PATH)

# Connect to MySQL
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Drop table if exists
cursor.execute("DROP TABLE IF EXISTS uploaded_data")

# Create table dynamically
columns = ", ".join([f"`{col}` TEXT" for col in df.columns])
cursor.execute(f"CREATE TABLE uploaded_data ({columns})")

# Insert data
for _, row in df.iterrows():
    values = "', '".join([str(x) for x in row.values])
    cursor.execute(f"INSERT INTO uploaded_data VALUES ('{values}')")

conn.commit()
cursor.close()
conn.close()

print("✅ Dataset uploaded to MySQL successfully")