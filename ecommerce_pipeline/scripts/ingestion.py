#moving data from sources to Azure Data Factory

import pandas as pd

df = pd.read_csv("D:/Work/MS Azure/Projects/ecommerce pipeline/data/ecommerce_electronics.csv")
df.to_csv("D:/Work/MS Azure/Projects/ecommerce pipeline/data lake/raw/ecommerce_electronics.csv",index = False)

print("Data moved to raw layer")