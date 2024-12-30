import os
import pandas as pd
import mysql.connector
import logging
from sqlalchemy import create_engine


# Configure logging
logging.basicConfig(
    filename='../logs/etl_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_etl():
    try:
        logging.info("Starting ETL process")

         # Create SQLAlchemy engine for MySQL connection
        engine = create_engine("mysql+mysqlconnector://root:R6%40#Siege@localhost/sales_data_pipeline")
        logging.info("Database connection established using SQLAlchemy")


        # Define the SQL query
        query = """
        SELECT 
            s.id,
            s.sale_date,
            p.product_name,
            p.category,
            r.region_name,
            s.quantity,
            s.price,
            s.total
        FROM 
            sales s
        JOIN 
            products p ON s.product_id = p.product_id
        JOIN 
            regions r ON s.region_id = r.region_id
        """

        # Execute the query and load data into a Pandas DataFrame
        df = pd.read_sql(query, engine)
        logging.info("Data successfully retrieved from database")

        # Perform transformations (example: ensure proper datatypes)
        df['sale_date'] = pd.to_datetime(df['sale_date'])
        df['total'] = df['quantity'] * df['price']  # Recalculate total for validation
        logging.info("Data transformations completed")

        # Save the transformed data to a CSV file
        output_path = '../data/transformed_sales_data.csv'
        df.to_csv(output_path, index=False)
        logging.info(f"Transformed data saved to {output_path}")

        print("ETL process completed successfully!")
        logging.info("ETL process completed successfully")

    except mysql.connector.Error as db_err:
        logging.error(f"Database error: {db_err}")
        print(f"ETL process failed: {db_err}")

    except Exception as e:
        logging.error(f"General error: {e}")
        print(f"ETL process failed: {e}")

    finally:
        # No need to explicitly close the connection with SQLAlchemy
        logging.info("ETL process ended")

if __name__ == "__main__":
    run_etl()
