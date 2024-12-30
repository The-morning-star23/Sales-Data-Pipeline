import os
import pandas as pd
import mysql.connector
import logging

# Setup logging
logging.basicConfig(
    filename='../logs/etl_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ensure the data directory exists
output_dir = '../data'
os.makedirs(output_dir, exist_ok=True)

# Database connection settings
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'sales_data'
}

try:
    logging.info("Starting ETL process.")
    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    query = "SELECT * FROM raw_sales_data"
    
    # Read data from the database
    df = pd.read_sql(query, connection)
    logging.info("Data successfully fetched from database.")

    # Perform transformations
    df['Sales'] = df['Quantity'] * df['Price']
    transformed_data = df[['Date', 'Region', 'Product', 'Quantity', 'Sales']]
    
    # Save the transformed data to CSV
    output_file = os.path.join(output_dir, 'transformed_sales_data.csv')
    transformed_data.to_csv(output_file, index=False)
    logging.info(f"Transformed data saved to {output_file}.")

except Exception as e:
    logging.error(f"ETL process failed: {e}")
    print(f"ETL process failed: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        logging.info("Database connection closed.")
