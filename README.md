# ETL Pipeline with Apache Airflow and SQLite/PostgreSQL

## 📌 Project Overview
This project demonstrates how to build an **ETL (Extract, Transform, Load) pipeline** using **Apache Airflow** to orchestrate data workflows.  
The pipeline extracts data from multiple sources (CSV files, JSON files, and APIs), transforms the data, and loads it into a relational database such as **PostgreSQL** or **SQLite**.

The goal of this project is to showcase data engineering fundamentals, workflow orchestration, and automation using Airflow.

---

## 🏗️ Architecture
**Data Sources → Airflow DAG → Transformations → Relational Database**

- **Extract**
  - CSV files
  - JSON files
  - Public APIs
- **Transform**
  - Data cleaning
  - Type conversions
  - Removing duplicates
  - Normalization
- **Load**
  - PostgreSQL or SQLite database

---

## 🛠️ Technologies Used
- **Apache Airflow** – Workflow orchestration
- **Python** – ETL logic
- **Pandas** – Data transformation
- **SQLite / PostgreSQL** – Data storage
- **SQLAlchemy** – Database connection
- **Docker (optional)** – Containerized Airflow setup

---

## 📂 Project Structure  
etl-airflow-pipeline/  
│  
├── dags/  
│ └── etl_pipeline_dag.py  
│
├── data/
│ ├── raw/
│ │ ├── sample.csv
│ │ └── sample.json
│ └── processed/
│
├── scripts/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── database/
│ └── etl.db
│
├── requirements.txt
├── docker-compose.yml
└── README.md
