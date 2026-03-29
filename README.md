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

The repository follows a simple medallion-style layout (raw, processed, curated) commonly used in modern data lakehouse architectures.[web:9][web:10]

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
   - Raw data is copied as-is into `data_lake/raw` to preserve the original source.[web:3][web:5][web:10]

2. **Transformation (Raw to Processed/Curated)**  
   - `transform.py` cleans, validates, and enriches the raw data (types, missing values, derived fields).  
   - Clean data is written to `data_lake/processed`, and aggregated/modelled tables are written to `data_lake/curated` (for example, daily revenue, top products, customer metrics).[web:5][web:9][web:10]

3. **Load (Curated to Warehouse)**  
   - `load.py` loads curated tables into `warehouse.db` (SQLite) to simulate loading into a cloud data warehouse such as Azure Synapse or Azure SQL Database.[web:5][web:9]

---

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` for installing dependencies
- SQLite (bundled with most Python installations via the `sqlite3` module)[web:5][web:11]

(Optional Azure alignment: In a cloud deployment, these components would map to Azure Data Lake Storage, Azure Data Factory/Databricks for orchestration and transformation, and Azure Synapse Analytics for warehousing.)[web:3][web:5][web:9]

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/Ecommerce_Data_pipeline.git
   cd Ecommerce_Data_pipeline
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies (example):

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Pipeline

You can run the pipeline end-to-end or step by step.

### 1. Ingest raw data

```bash
python scripts/ingestion.py
```

- Reads `data/orders.csv`.  
- Writes raw copies into `data_lake/raw` (e.g., `orders_raw.csv`).[web:3][web:5]

### 2. Transform data

```bash
python scripts/transform.py
```

- Cleans and standardizes the raw data (schemas, data types, derived metrics).  
- Outputs processed datasets to `data_lake/processed` and curated analytics tables to `data_lake/curated`.[web:5][web:9][web:10]

### 3. Load curated data into the warehouse

```bash
python scripts/load.py
```

- Loads curated tables into `warehouse.db` (SQLite).  
- After loading, you can connect with any SQLite browser or BI tool to run queries.[web:5][web:9][web:11]

Example query (using `sqlite3` CLI):

```bash
sqlite3 warehouse.db
SELECT order_date, SUM(total_amount) AS daily_revenue
FROM fact_orders
GROUP BY order_date
ORDER BY order_date;
```

---

## Use Cases

This project is designed as a learning and portfolio-friendly example for:

- Practicing core data engineering patterns (ingest, transform, load, medallion layers).  
- Prototyping an Azure-style e-commerce analytics pipeline locally before deploying to the cloud.  
- Demonstrating end-to-end data flow in interviews or technical blogs.[web:5][web:8][web:9][web:11]

---

## Possible Azure Mapping

While the implementation here is local, you can map each layer to managed Azure services:[web:3][web:5][web:9]

- **Data Lake** → Azure Data Lake Storage Gen2.  
- **Orchestration & Ingestion** → Azure Data Factory, Azure Logic Apps, or Azure Databricks jobs.[web:2][web:3][web:4][web:5]  
- **Transformations** → Azure Databricks or Azure Synapse Spark pools.[web:5][web:9]  
- **Warehouse** → Azure Synapse Dedicated SQL Pool or Azure SQL Database.[web:5][web:9]

This makes the repository a good starting point for designing an end-to-end Azure-based e-commerce analytics solution.[web:5][web:9][web:10][web:11]

---

## Future Improvements

- Add unit tests for each script (`ingestion.py`, `transform.py`, `load.py`).  
- Introduce configuration files (YAML/JSON) to manage paths and parameters.  
- Replace local scheduling with orchestration (e.g., Azure Data Factory pipelines or GitHub Actions).  
- Extend the schema to include customers, products, and inventory to support richer analytics and dashboards.[web:5][web:8][web:9][web:11]

---

## License

Add your preferred license here (for example, MIT) so others know how they can use and contribute to this project.[web:11]
