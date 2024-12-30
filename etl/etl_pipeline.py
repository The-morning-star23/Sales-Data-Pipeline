import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    database='sales_data_pipeline',
    user='root',
    password='R6@#Siege'
)

query = """
SELECT s.sale_date, p.product_name, r.region_name, s.quantity, s.price, s.total
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN regions r ON s.region_id = r.region_id
"""

df = pd.read_sql(query, connection)

# Transform: Add additional features
df['month'] = pd.to_datetime(df['sale_date']).dt.strftime('%Y-%m')

# Save transformed data
df.to_csv('../data/transformed_sales_data.csv', index=False)
print("ETL Process Complete: Data saved to transformed_sales_data.csv")
