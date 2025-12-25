import os
import json
import mysql.connector
from datetime import datetime


TESTS_DIR = "tests"
REPORT_PATH = "reports/data_quality_report.txt"


def load_db_config():
    with open("data_cleaning_automation/config/db_config.json", "r") as f:
        return json.load(f)


def run_test(cursor, sql_file):
    with open(sql_file, "r") as f:
        query = f.read()

    cursor.execute(query)
    results = cursor.fetchall()

    return len(results) == 0


def main():
    db_config = load_db_config()
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_lines = [
        "AUTOCLEANR — DATA QUALITY REPORT",
        f"Generated at: {now}",
        "-" * 40
    ]

    all_passed = True

    for file in sorted(os.listdir(TESTS_DIR)):
        if file.endswith(".sql"):
            path = os.path.join(TESTS_DIR, file)
            passed = run_test(cursor, path)

            status = "PASS" if passed else "FAIL"
            report_lines.append(f"{file}: {status}")

            if not passed:
                all_passed = False

    report_lines.append("-" * 40)
    report_lines.append(
        "FINAL RESULT: ALL TESTS PASSED "
        if all_passed
        else "FINAL RESULT: SOME TESTS FAILED "
    )

    cursor.close()
    conn.close()

    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\n Report generated at: {REPORT_PATH}\n")


if __name__ == "__main__":
    main()

