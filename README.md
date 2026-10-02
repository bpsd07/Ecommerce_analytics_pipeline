# E-Commerce Analytics Pipeline

## Project Overview
This project is an end-to-end data analytics pipeline designed to process, analyze, and visualize retail sales data. It demonstrates the complete lifecycle of a data engineering and business intelligence workflow—from raw data ingestion to interactive dashboarding.

The pipeline ingests raw CSV data, cleans and normalizes it using Python, loads it into a relational SQL database, and connects to Power BI for dynamic visualization.

## Tech Stack & Skills Demonstrated
*   **Python (`pandas`, `sqlite3`):** Data extraction, cleaning, transformation (ETL), and database connection scripting.
*   **SQL (SQLite):** Database creation, table schemas, and data aggregation queries.
*   **Power BI:** Direct-query dashboarding via Python integration, data visualization, and KPI tracking.
*   **Excel:** Initial data exploration, validation, and baseline pivot table analysis.
*   **Git/GitHub:** Version control and project deployment.

## Project Architecture
1.  **Phase 1: Data Exploration (Excel)** - Initial review of the raw Sample Superstore dataset to identify missing values, formatting inconsistencies, and baseline metrics using Pivot Tables.
2.  **Phase 2: Data Cleaning (Python)** - A `pandas` script (`clean.py`) normalizes column headers, removes duplicate entries, handles null values, and exports a production-ready CSV.
3.  **Phase 3: Database Storage (SQL)** - A Python loader script (`load_sql.py`) automatically generates a SQLite database (`ecommerce.db`), creates the `sales` table, and inserts the cleaned records.
4.  **Phase 4: Business Intelligence (Power BI)** - Power BI connects directly to the SQLite database using a custom Python script to fetch real-time query results and power an interactive sales dashboard.

## Repository Structure
\`\`\`text
ecommerce-analytics-pipeline/
│
├── 1_raw_data/              # Original, unmodified datasets (Ignored in Git)
├── 2_cleaned_data/          # Processed data ready for database insertion (Ignored in Git)
├── 3_python_scripts/        
│   ├── clean.py             # ETL script for cleaning data
│   └── load_sql.py          # Script to build database and execute SQL queries
├── 4_sql_dbs/               # SQLite database files (Ignored in Git)
├── README.md                # Project documentation
└── ECommerce_Dashboard.pbix # Power BI visualization file
\`\`\`

## How to Run Locally
1.  Clone this repository: `git clone https://github.com/bpsd07/Ecommerce_analytics_pipeline.git`
2.  Install the required Python packages: `pip install pandas matplotlib`
3.  Place your raw `superstore.csv` file inside the `1_raw_data` folder.
4.  Run the cleaning script: `cd 3_python_scripts && python clean.py`
5.  Run the SQL loader: `python load_sql.py`
6.  Open the `.pbix` file in Power BI to view the dashboard (Ensure your Python path is configured in Power BI settings).

## Future Enhancements
*   Implement advanced SQL Window Functions for month-over-month growth analysis.
*   Expand the Power BI dashboard to include geographic mapping and profit margin analysis.
*   Automate the pipeline execution using a simple batch script or cron job.
