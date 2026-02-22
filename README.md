# Data Practice Datasets

A curated collection of demo datasets for practicing **Data Engineering**, **ETL/ELT**, **PySpark**, and **Lakehouse** workflows.

This repository is designed for hands-on learning and project prototyping. It includes CSV, JSON, and raw files across multiple domains, along with data generation scripts to help you create synthetic datasets for demos and testing.

## 📦 What You’ll Find

- **Practice-ready datasets** for common data engineering scenarios.
- **Structured and semi-structured formats** (CSV, JSON, raw files).
- **Domain-oriented sample data** (banking, sales, flight booking, and more).
- **Data generation scripts** for creating large or custom demo datasets.

## 📁 Repository Structure

- `banking/` – Banking-related datasets and advanced PySpark scenario scripts.
- `bankof420/` – Additional banking demo datasets.
- `sales/` – Sales, trips, drivers, locations, and payment datasets.
- `flightbooking/` – Flight booking dimensions/facts and incremental/SCD-style samples.
- `CSV/` – General CSV practice files.
- `JSON/` – JSON format datasets.
- `RAW/` – Raw source-style files for ingestion practice.
- `DATA_GENERATION_SCRIPTS/` – Scripts to generate synthetic demo data.

## 🚀 How to Use

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd data-practice-datasets
   ```
2. Pick a dataset folder based on your use case.
3. Load files into your preferred tool (PySpark, Pandas, SQL engine, Databricks, etc.).
4. Build pipelines for ingestion, cleaning, transformation, and analytics.

## 🧪 Suggested Practice Use Cases

- Batch ingestion pipelines (CSV/JSON to bronze/silver/gold).
- Incremental loads and merge/upsert workflows.
- Schema evolution and semi-structured parsing.
- Data quality validation checks.
- Join optimization, partitioning, and performance tuning in Spark.

## 🛠 Data Generation Scripts

The `DATA_GENERATION_SCRIPTS/` directory contains scripts that can be used to generate additional demo data.

> Note: Some scripts may expect local dependencies (for example database connectors or Faker). Install required packages and configure local database settings before running them.

## 🤝 Contributing

Contributions are welcome. You can contribute by:

- Adding new realistic datasets.
- Improving data quality and documentation.
- Adding reproducible data generation scripts.
- Providing project ideas and exercises based on these datasets.

## 📄 License

Use these datasets for learning, experimentation, and demo projects. If you plan to use them for production or redistribution, please review and apply an appropriate license policy for your organization.
