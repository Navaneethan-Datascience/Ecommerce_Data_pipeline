from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("ETL") \
    .config("spark.hadoop.hadoop.native.lib", "false") \
    .getOrCreate()

df = spark.read.csv(
    "D:/Work/MS Azure/Projects/ecommerce pipeline/data lake/raw/ecommerce_electronics.csv",
    header=True,
    inferSchema=True
)

df_unique = df.dropDuplicates(["OrderID"])

df_filtered = df_unique.filter(
    (col("TotalAmount") > 0) & (col("quantity") > 0)
)

print("Row count:", df_filtered.count())


df_filtered.write.mode("overwrite").option("header", True).csv( "D:/Work/MS Azure/Projects/ecommerce pipeline/data lake/processed/ecommerce_cleaned")


print("Data cleaned, deduplicated, and stored")