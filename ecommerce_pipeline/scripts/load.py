import sqlite3
import pandas as pd

connection = sqlite2.connect("warehouse.db")

df = pd.read_csv("D:/Work/MS Azure/Projects/ecommerce pipeline/data lake/ecommerce_cleaned.csv")
df.to_sql("orders",conn,if_exists="replace",index=False)

print("Loaded into the warehouse")