import pandas as pd
import mysql.connector
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "db_config.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "cleaned_table.csv")

with open(CONFIG_PATH) as f:
    config = json.load(f)

conn = mysql.connector.connect(**config)

query = "SELECT * FROM clean_table"
df = pd.read_sql(query, conn)

df.to_csv(OUTPUT_PATH, index=False)

conn.close()

print("✅ Cleaned data exported to output/cleaned_table.csv")

