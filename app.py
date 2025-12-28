import streamlit as st
import pandas as pd
import subprocess
import os

st.set_page_config(page_title="Autocleanr", layout="wide")

st.title("🧹 Autocleanr")
st.caption("SQL-first, schema-agnostic data cleaning engine")

st.sidebar.header("Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

run_engine = st.sidebar.button("Run Cleaning Engine")
run_tests = st.sidebar.button("Run Validation & Report")

ENGINE_DATA_PATH = "data_cleaning_automation/data/sample.csv"
CLEANED_OUTPUT_PATH = "data_cleaning_automation/output/cleaned_table.csv"
REPORT_PATH = "reports/data_quality_report.txt"

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.to_csv(ENGINE_DATA_PATH, index=False)

    st.subheader("📄 Raw Data Preview")
    st.dataframe(df.head(50), use_container_width=True)

if run_engine:
    st.info("Running cleaning engine...")
    subprocess.run(["python", "engine/runall.py"])
    st.success("Cleaning completed successfully")

if run_tests:
    st.info("Running validation tests...")
    subprocess.run(["python", "scripts/generate_report.py"])
    st.success("Validation completed")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ Cleaned Data")
    if os.path.exists(CLEANED_OUTPUT_PATH):
        clean_df = pd.read_csv(CLEANED_OUTPUT_PATH)
        st.dataframe(clean_df.head(50), use_container_width=True)
    else:
        st.warning("Cleaned data not available yet")

with col2:
    st.subheader("📊 Data Quality Report")
    if os.path.exists(REPORT_PATH):
        with open(REPORT_PATH) as f:
            report_text = f.read()
        st.code(report_text)
    else:
        st.warning("Report not generated yet")
