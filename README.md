*AUTOCLEANR!!*

IDEA!?
To build a tool that automatically cleans messy datasets using SQL orchestrated by python. 

how did the bulb glow? my prior project was all DATA CLEANING AND EXPLOTATORY DATA ANALYSIS all thru SQL. and i thought why not AUTOMATE it!?

**pic of the idea-page hand written notes**
autocleanr\data_cleaning_automation\images\idea-page.jpeg

how does autocleanr work?
1.Upload CSV via UI
2.Load data into MySQL (uploaded_data)
3.Apply SQL cleaning rules
4.Materialize cleaned table (clean_table)
5.Run automated SQL validation tests
6.Generate data quality report
7.Export cleaned data to CSV

**pic of the workflow**
autocleanr\data_cleaning_automation\images\workflow.jpeg


storyy floww of the project:

Autocleanr was built around a simple observation: most data projects spend more time cleaning data than using it. While working on SQL-based data cleaning workflows, it became clear that these steps were repetitive, deterministic, and well-suited for automation rather than manual scripting.

The project is designed with a clear separation of concerns. Python acts as the orchestration layer, managing file ingestion, execution order, and automation, while SQL performs all data cleaning operations directly inside the database. This mirrors real-world data pipelines, where transformations are pushed as close to the data as possible for efficiency and scalability.

Autocleanr includes automated, schema-agnostic SQL validation tests that verify pipeline correctness after each run, along with a human-readable data quality report that serves as proof of execution. A lightweight Streamlit UI exposes the pipeline for interactive use, allowing users to upload datasets, run cleaning, inspect outputs, and view validation results.

The project prioritizes clarity, correctness, and portability over complexity. It demonstrates how disciplined architecture, database-centric transformations, and automated validation can turn routine data cleaning into a reliable and observable system—while laying a clean foundation for future scaling and intelligence.

contact me if you wanna know more about this project!!

👩‍💻 Author

Sandhiya Laxmi
Data Engineering & Applied AI Enthusiast