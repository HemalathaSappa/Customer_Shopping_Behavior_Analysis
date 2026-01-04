from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:Hema%40123@localhost:3306/customer_shopping_behavior"
)

# Test connection
df = pd.read_sql("SHOW TABLES;", engine)
print("✅ Connected to MySQL")
print(df)
