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

the story flowwwwwwwww... (might help someone who is creating this)

Once the flow was clear, the next challenge was separation of responsibility.
This project has two different worlds:
Python → automation, orchestration, file handling
SQL → actual data cleaning logic

So instead of mixing everything in one place, the project is deliberately split into layers:
Python scripts only move data and trigger actions
SQL files only define how data is cleaned

This makes the project:
easier to understand
easier to debug
closer to how real-world data pipelines are built

why python + sql and not just one?
Python is great at:
reading CSV files
automating workflows
connecting systems together
But Python (pandas) works in application memory, which means:
limited by RAM
slower for very large datasets

SQL, on the other hand:

runs inside the database
is optimized for large datasets
uses indexes and query planners
scales much better

So Autocleanr uses Python as the conductor and SQL as the worker.

Python tells what to do.
SQL decides how to do it efficiently.
about credentials & security (important design decision)
To connect Python and MySQL, database credentials are required.
Hardcoding credentials inside scripts is unsafe and unprofessional, especially for public repositories.
So this project uses:
*db_config.json → stores DB credentials locally
*.gitignore → ensures sensitive files are never pushed to GitHub
*db_config_example.json → helps others understand the structure without exposing secrets

This design:

keeps credentials secure
allows portability across systems
prevents accidental data leaks
The same idea is applied to datasets and outputs:
real datasets stay private
real outputs stay local
only sample outputs are shared for transparency
why output_example exists
Since the actual dataset and output are ignored, someone viewing the repository might wonder:
“What does this tool actually produce?”
That’s why -- output_example/ exists.
It acts as:
proof that the pipeline works
a reference for expected output
documentation through data

how the pipeline actually runs
Everything is tied together using a single entry point:
--python runall.py
When this command is executed:

Python reads the CSV file
Uploads it into MySQL as a raw table
Executes SQL cleaning scripts step by step
Fetches the cleaned table back
Saves the cleaned dataset as a CSV file

This simulates a real ETL-style pipeline, even though the project is intentionally kept simple.

Autocleanr currently supports:
Trimming unwanted spaces
Handling NULL and empty values
Removing duplicate records
Exporting cleaned datasets

final note

Autocleanr is not about replacing SQL or Python.
It’s about using each tool for what it does best
and building a clean, scalable, and understandable data cleaning pipeline.

