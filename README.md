*AUTOCLEANR!!*

IDEA!?
To build a tool that automatically cleans messy datasets using SQL orchestrated by python. 

how did the bulb glow? my prior project was all DATA CLEANING AND EXPLOTATORY DATA ANALYSIS all thru SQL. and i thought why not AUTOMATE it!?

**pic of the idea-page hand written notes**
autocleanr\data_cleaning_automation\images\idea-page.jpeg

how does autocleanr work?
1. User provides a CSV dataset
2. Python uploads raw data into MySQL
3. SQL scripts clean the data:
   - Trim spaces
   - Handle NULLs
   - Remove duplicates
4. Python downloads the cleaned table
5. Cleaned output is exported as CSV

**pic of the workflow**
autocleanr\data_cleaning_automation\images\workflow.jpeg

autocleanr/
│
├── data_cleaning_automation/
│   ├── config/          # DB credentials (ignored)
│   ├── data/            # Raw datasets (ignored)
│   ├── scripts/         # Python orchestration
│   ├── sql/             # SQL cleaning logic
│   ├── output_example/  # Sample cleaned output
│
├── .gitignore
├── README.md

storyy floww of the project:

Autocleanr began with a simple observation: most data projects spend more time cleaning data than using it. After working on a data cleaning and exploratory analysis project entirely in SQL, it became clear that the work was repetitive, predictable, and well-suited for automation. The idea was not to invent a new cleaning technique, but to systematize a process that databases already do well.

Before writing code, the focus was on defining the flow. Autocleanr is built around a clear separation of responsibilities. Python acts as the orchestration layer, handling file ingestion, execution order, and automation. SQL acts as the transformation engine, performing all data cleaning operations directly inside the database. This separation avoids tightly coupled scripts and reflects how production-grade data pipelines are structured.

The choice to combine Python and SQL was intentional. Python excels at workflow control and system integration, but data cleaning libraries operate in application memory and do not scale efficiently for large structured datasets. SQL, in contrast, executes inside the database engine, benefits from query optimization and indexing, and scales naturally as data grows. In Autocleanr, Python serves as the conductor, coordinating the pipeline, while SQL performs the heavy lifting.

Security and portability were treated as first-class concerns. Database credentials are stored locally and excluded from version control using .gitignore, while example configuration files are provided to document structure without exposing secrets. The same principle applies to data outputs: real datasets and outputs remain local, while a curated example output is included to demonstrate the pipeline’s behavior.

Execution is driven through a single entry point. Running python runall.py triggers a deterministic workflow: raw CSV data is ingested into MySQL, SQL-based cleaning transformations are applied in sequence, and the cleaned data is materialized back as a CSV file. While intentionally lightweight, this flow mirrors an ETL-style pipeline used in real data engineering systems.

At its current stage, Autocleanr supports trimming, null normalization, duplicate removal, and clean data export. The project is not about replacing SQL or Python, but about using each tool where it is strongest to build a scalable, understandable, and disciplined data cleaning pipeline.


