# Azure E-commerce Data Pipeline

This repository contains an end-to-end **data** pipeline for an e-commerce platform, inspired by a modern Azure data engineering stack and medallion architecture (raw → processed → curated). The goal is to simulate how orders data flows from source files into a data lake and finally into an analytics-ready warehouse.
---

## Project Overview

The project demonstrates a simplified version of an Azure-centric e-commerce analytics pipeline using local files and scripts:[web:5][web:9]

- Land raw e-commerce orders data into a `data_lake/raw` zone.
- Clean and transform the data into the `data_lake/processed` zone.
- Aggregate and model data into curated tables in `data_lake/curated`.
- Load curated data into a warehouse (`warehouse.db`) that can be queried by BI tools or downstream applications.

Although this implementation runs locally with Python scripts and a SQLite warehouse, the structure mirrors real-world Azure services such as Azure Data Lake Storage, Azure Data Factory, and Azure Synapse/Databricks.

---

## Architecture and Folder Structure

The repository follows a simple medallion-style layout (raw, processed, curated) commonly used in modern data lakehouse architectures.

```bash
Ecommerce_pipeline/
│
├── data_lake/
│    ├── raw/          # Landing zone for raw source data (e.g., CSV exports, API dumps)
│    ├── processed/    # Cleaned and standardized datasets
│    ├── curated/      # Aggregated, analytics-ready datasets (facts, dimensions)
│
├── scripts/
│    ├── ingestion.py  # Extract & load raw data into the raw zone
│    ├── transform.py  # Transform raw data into processed & curated layers
│    ├── load.py       # Load curated data into the warehouse (SQLite)
│
├── data/
│    └── orders.csv    # Sample e-commerce orders source data
│
├── warehouse.db       # SQLite warehouse for analytics/BI consumption
```

---

## Data Flow

1. **Ingestion (Landing to Raw)**  
   - `ingestion.py` reads source files such as `data/orders.csv`.  
   - Raw data is copied as-is into `data_lake/raw` to preserve the original source.
     
2. **Transformation (Raw to Processed/Curated)**  
   - `transform.py` cleans, validates, and enriches the raw data (types, missing values, derived fields).  
   - Clean data is written to `data_lake/processed`, and aggregated/modelled tables are written to `data_lake/curated` (for example, daily revenue, top products, customer metrics).

3. **Load (Curated to Warehouse)**  
   - `load.py` loads curated tables into `warehouse.db` (SQLite) to simulate loading into a cloud data warehouse such as Azure Synapse or Azure SQL Database.
   
---

## Running the Pipeline

You can run the pipeline end-to-end or step by step.

### 1. Ingest raw data

```bash
python scripts/ingestion.py
```

- Reads `data/orders.csv`.  
- Writes raw copies into `data_lake/raw` (e.g., `orders_raw.csv`).
  
### 2. Transform data

```bash
python scripts/transform.py
```

- Cleans and standardizes the raw data (schemas, data types, derived metrics).  
- Outputs processed datasets to `data_lake/processed` and curated analytics tables to `data_lake/curated`.
  
### 3. Load curated data into the warehouse

```bash
python scripts/load.py
```

- Loads curated tables into `warehouse.db` (SQLite).  
- After loading, you can connect with any SQLite browser or BI tool to run queries.

---

## Use Cases

This project is designed as a learning and portfolio-friendly example for:

- Practicing core data engineering patterns (ingest, transform, load, medallion layers).  
- Prototyping an Azure-style e-commerce analytics pipeline locally before deploying to the cloud.  
- Demonstrating end-to-end data flow in interviews or technical blogs.

---

## Possible Azure Mapping

While the implementation here is local, you can map each layer to managed Azure services:

- **Data Lake** → Azure Data Lake Storage Gen2.  
- **Orchestration & Ingestion** → Azure Data Factory, Azure Logic Apps, or Azure Databricks jobs.
- **Transformations** → Azure Databricks or Azure Synapse Spark pools.  
- **Warehouse** → Azure Synapse Dedicated SQL Pool or Azure SQL Database.

## Gained Knowledge

- Learned how to structure a data pipeline with raw, processed, and curated layers.
- Practiced building ETL steps using separate Python scripts for ingestion, transform, and load.
- Understood how a local pipeline (files + SQLite) relates to Azure data services in the cloud.
- Improved my skills in organizing a data engineering project with a clear folder and script structure.
- Gained experience handling data quality issues while moving data from source to analytics-ready tables.
