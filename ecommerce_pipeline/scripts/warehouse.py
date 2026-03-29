from sqlalchemy import create_engine

#creating warehouse table
engine = create_engine("sqlite://warehouse.db")

print("warhouse.db created")