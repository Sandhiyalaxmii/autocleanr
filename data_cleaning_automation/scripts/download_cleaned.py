# download cleaned data
import pandas as pd
import mysql.connector
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_PATH = os.path.join(BASE_DIR, "output", "cleaned_output.csv")
CONFIG_PATH = os.path.join(BASE_DIR, "config", "db_config.json")

with open(CONFIG_PATH) as f:
    config = json.load(f)

conn = mysql.connector.connect(**config)

df = pd.read_sql("SELECT * FROM uploaded_data", conn)
df.to_csv(OUTPUT_PATH, index=False)

conn.close()

print("✅ Cleaned data exported to output/cleaned_output.csv")
