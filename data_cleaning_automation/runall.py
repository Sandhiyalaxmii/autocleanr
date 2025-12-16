import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

def run(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    subprocess.run([sys.executable, script_path], check=True)

print("Starting AutoCleanr pipeline")

run("upload_to_mysql.py")
run("clean_with_mysql.py")
run("download_cleaned.py")

print("AutoCleanr pipeline completed successfully")

