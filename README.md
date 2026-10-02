<div align="center">

# 📊 E-Commerce Analytics Pipeline

### *An End-to-End Enterprise Data Engineering & Business Intelligence Workflow*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)]()

<p align="center">
  <a href="#-project-overview">Overview</a> •
  <a href="#-system-architecture--workflow">Architecture</a> •
  <a href="#-data-pipeline-lifecycle">Pipeline Lifecycle</a> •
  <a href="#-repository-structure">Structure</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-sql-analytics--kpis">Analytics & KPIs</a> •
  <a href="#-author">Author</a>
</p>

---

</div>

## 📌 Project Overview

The **E-Commerce Analytics Pipeline** is an automated, production-style data pipeline designed to transform raw, transactional retail sales data into clean, structured datasets, load them into a relational SQL database, and deliver high-impact executive dashboards via **Microsoft Power BI**.

This repository showcases core data engineering and BI competencies:
- **Automated Data Extraction & Cleansing**: Standardization of raw CSV records, deduplication, null-handling, and column normalization via Python (`pandas`).
- **Relational Storage & Schema Management**: Structured ingestion into an optimized SQLite database (`ecommerce.db`).
- **SQL-Driven Aggregations**: Performant SQL queries calculating revenue, profit margins, and sales distributions across product categories.
- **Interactive BI Dashboarding**: Power BI reporting with dynamic category breakdowns, regional sales distributions, and discount sensitivity tracking.

---

## 🏗️ System Architecture & Workflow

The end-to-end data lifecycle moves systematically across four distinct operational stages:

```mermaid
flowchart TD
    subgraph S1["1. Raw Ingestion"]
        A["📁 1_raw_data/superstore.csv<br/>(Transactional Sales Records)"]
        B["📁 1_raw_data/superstore.xlsx<br/>(Legacy Workbook Backup)"]
    end

    subgraph S2["2. Automated ETL & Wrangling"]
        C["🐍 3_python_scripts/clean.py<br/>(Pandas Engine)"]
        C1["Header Normalization<br/>(snake_case)"]
        C2["Deduplication &<br/>Null Value Handling"]
        C3["Type Casting & Sanitization"]
        D["📁 2_cleaned_data/clean_superstore.csv<br/>(Standardized Output)"]
    end

    subgraph S3["3. Relational Storage & SQL Engine"]
        E["🐍 3_python_scripts/load_sql.py<br/>(SQLite Ingestion Script)"]
        F[("🗄️ 4_sql_dbs/ecommerce.db<br/>(Relational SQLite Store)")]
        G["📊 SQL Queries & Aggregations<br/>(Revenue & Category Metrics)"]
    end

    subgraph S4["4. Business Intelligence & Analytics"]
        H["📈 Sales_by_category.pbix<br/>(Power BI Interactive Dashboard)"]
        H1["Category Revenue Breakdown"]
        H2["Regional Performance Analysis"]
        H3["Profit & Discount KPIs"]
    end

    A --> C
    B -.-> C
    C --> C1 --> C2 --> C3 --> D
    D --> E
    E --> F
    F --> G
    F --> H
    H --> H1 & H2 & H3

    style S1 fill:#f8f9fa,stroke:#6c757d,stroke-width:2px
    style S2 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style S3 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style S4 fill:#fff8e1,stroke:#ffa000,stroke-width:2px
```

### 🔄 Data Transformation Lifecycle

```mermaid
sequenceDiagram
    autonumber
    participant Raw as Raw Data Source
    participant ETL as Python (clean.py)
    participant Staging as Cleaned CSV Store
    participant DB as SQLite (load_sql.py)
    participant BI as Power BI Dashboard

    Raw->>ETL: Ingest raw superstore.csv (Windows-1252 encoding)
    ETL->>ETL: Standardize column names to lower_snake_case
    ETL->>ETL: Drop duplicate rows and strip null values
    ETL->>Staging: Write clean_superstore.csv
    Staging->>DB: Read clean CSV & stream to SQLite
    DB->>DB: Create/replace 'sales' table schema
    DB->>DB: Execute aggregation query (Total Revenue by Category)
    DB-->>BI: Connect & load structured records
    BI-->>BI: Render executive KPI visualizations & slicers
```

---

## 📂 Repository Structure

```text
Ecommerce_analytics_pipeline/
│
├── 📁 1_raw_data/
│   ├── superstore.csv               # Raw transactional dataset (~9,995 records)
│   └── superstore.xlsx              # Raw Excel format backup
│
├── 📁 2_cleaned_data/
│   └── clean_superstore.csv         # Sanitized, production-ready dataset
│
├── 📁 3_python_scripts/
│   ├── clean.py                     # Data cleaning & normalization script
│   └── load_sql.py                  # Automated SQLite loader & analytics query
│
├── 📁 4_sql_dbs/
│   ├── .gitkeep                     # Keeps directory tracked in version control
│   └── ecommerce.db                 # Generated SQLite database (git-ignored)
│
├── 📊 Sales_by_category.pbix        # Interactive Power BI report & visual dashboard
├── 📄 .gitignore                    # Prevents binaries, caches & temp DBs from tracking
└── 📄 README.md                     # Comprehensive project documentation
```

---

## ⚙️ Data Pipeline Lifecycle

### 1. Ingestion & Raw Data Profiling
- **Source**: Retail sales transactional records with customer demographic, shipping, geographic, and financial parameters.
- **Attributes**:
  - `Ship Mode`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`
  - `Category`, `Sub-Category`, `Sales`, `Quantity`, `Discount`, `Profit`

### 2. Data Cleaning & Transformation (`clean.py`)
- **Encoding Handling**: Reads raw CSV with `windows-1252` encoding to prevent encoding corruptions.
- **Column Standardization**: Converts column headers to lowercase, replaces spaces and hyphens with underscores (`_`).
- **Data Integrity**: Removes exact duplicate entries and drops records with missing critical values.
- **Export**: Generates `clean_superstore.csv` inside `2_cleaned_data/`.

```python
# Core transformation logic in clean.py
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
df = df.drop_duplicates()
df = df.dropna()
```

### 3. Database Ingestion & Relational Modeling (`load_sql.py`)
- Connects to SQLite database `4_sql_dbs/ecommerce.db`.
- Loads the cleaned dataset into table `sales`.
- Executes SQL analytical aggregations to compute revenue by product line.

```sql
SELECT 
    category, 
    ROUND(SUM(sales), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales 
GROUP BY category
ORDER BY total_revenue DESC;
```

### 4. Business Intelligence Dashboard (`Sales_by_category.pbix`)
- **Power BI File**: [Sales_by_category.pbix](Sales_by_category.pbix)
- **Key Visualizations**:
  - **Category Performance**: Bar & column charts tracking sales volume and net profit.
  - **Profit Margin & Discount Impact**: Scatter & trend charts identifying products with negative margins under high discount rates.
  - **Regional Breakdown**: Geographical slicing across North, South, East, and West sales zones.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+**
- **Git**
- **Power BI Desktop** (Optional, for `.pbix` dashboard exploration)

### 1. Clone the Repository
```bash
git clone https://github.com/bpsd07/Ecommerce_analytics_pipeline.git
cd Ecommerce_analytics_pipeline
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Create and activate virtual environment
python -m venv venv

# Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# macOS / Linux:
source venv/bin/activate

# Install required packages
pip install pandas matplotlib
```

### 3. Run the ETL Pipeline
```bash
# Step 1: Clean and standardize raw data
cd 3_python_scripts
python clean.py

# Step 2: Ingest clean data into SQLite and run SQL analytics
python load_sql.py
```

### 4. Open the Power BI Dashboard
1. Launch **Power BI Desktop**.
2. Open [`Sales_by_category.pbix`](Sales_by_category.pbix).
3. Refresh data source connections if prompted.

---

## 📈 SQL Analytics & KPIs

The SQL layer enables immediate extraction of executive-level metrics:

| Product Category | Total Revenue ($) | Key Characteristics |
| :--- | :---: | :--- |
| **Technology** | **Highest** | Strongest margin driver, high average order value (AOV). |
| **Furniture** | **Moderate** | High shipping costs, vulnerable to margin compression from heavy discounts. |
| **Office Supplies** | **High Volume** | High transaction velocity, consistent repeat customer orders. |

### Sample Aggregation Query:
```sql
SELECT 
    category,
    sub_category,
    COUNT(*) AS total_orders,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS net_profit
FROM sales
GROUP BY category, sub_category
ORDER BY revenue DESC;
```

---

## 🔮 Future Roadmap

- [ ] **Data Warehouse Integration**: Migrate storage from SQLite to Google BigQuery or PostgreSQL.
- [ ] **Orchestration**: Implement Apache Airflow / Cloud Composer DAGs for automated, scheduled pipeline runs.
- [ ] **Data Quality Validation**: Integrate Great Expectations or Pydantic for automated schema checks and data quality gates.
- [ ] **CI/CD Pipeline**: Add GitHub Actions workflow for automated test runs on commit.

---

## 👤 Author

**BHANU PRATAP SINGH DEO**
- GitHub: [@bpsd07](https://github.com/bpsd07)
- Repository: [bpsd07/Ecommerce_analytics_pipeline](https://github.com/bpsd07/Ecommerce_analytics_pipeline)

---

<div align="center">
  <sub>Built with ❤️ for scalable, professional data engineering workflows.</sub>
</div>
