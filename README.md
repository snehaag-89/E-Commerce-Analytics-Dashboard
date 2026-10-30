# E-Commerce Sales and Business Analytics Pipeline

An end-to-end data analytics and engineering project that cleans, structures, loads, and analyzes e-commerce transaction data. The pipeline automates data transformation, stages records into a relational SQLite database, and executes targeted SQL queries to uncover revenue drivers, customer behavior, and sales trends.

---

## Project Overview
* Data Processing and Pipeline: Cleans raw transaction logs, handles missing values, standardizes data types, and prepares tabular records for relational modeling.
* Database Architecture: Loads processed structured data into an automated SQLite database instance (ecommerce.db).
* Analytical Insights: Runs SQL aggregation queries via Pandas to evaluate top revenue-generating products, order distributions, and transactional trends.

---

## Tech Stack
* Language: Python 3.x
* Database: SQLite3
* Libraries: Pandas, NumPy
* Tools: VS Code, Git, GitHub

---

## Repository Structure

Ecommerce_Analytics_Project/
├── data_prep.py                # Data cleaning, null handling, and preprocessing script
├── load_to_sql.py              # Database connection setup and automated tabular ingestion
├── query_analysis.py           # SQL business queries executed via Pandas integration
├── cleaned_ecommerce_sales.csv # Processed dataset ready for relational loading
├── ecommerce.db                # Auto-generated SQLite relational database file
├── .gitignore                  # Excludes large binaries/CSVs and local environment files
└── README.md                   # Complete project documentation

---

## Architecture and Workflow

[Raw E-Commerce Data] 
       │
       ▼
 [data_prep.py] ────────► [cleaned_ecommerce_sales.csv]
                                    │
                                    ▼
                             [load_to_sql.py]
                                    │
                                    ▼
                           [SQLite: ecommerce.db]
                                    │
                                    ▼
                          [query_analysis.py] ────────► [Actionable Business Metrics]

1. Pre-processing (data_prep.py):
   * Drops duplicates, normalizes date formats, and strips irregular text fields.
   * Exports an optimized structured dataset (cleaned_ecommerce_sales.csv).

2. Database Ingestion (load_to_sql.py):
   * Establishes a local SQLite engine connection.
   * Maps CSV records directly into relational tables with appropriate schema definitions.

3. Query Engine and Analytics (query_analysis.py):
   * Uses pd.read_sql_query() to execute analytical queries directly against the database.
   * Pulls top-performing categories, monthly revenue changes, and high-frequency order metrics.

---

## Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/](https://github.com/)<username>/Ecommerce_Analytics_Project.git
cd Ecommerce_Analytics_Project