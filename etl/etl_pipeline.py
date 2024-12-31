import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import logging

# Load environment variables
load_dotenv()

# Configure logging
LOG_DIR = '../logs'
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure log directory exists
logging.basicConfig(
    filename=f'{LOG_DIR}/etl_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_etl():
    try:
        logging.info("Starting ETL process")

        # Database connection details
        username = os.getenv("DB_USER", "root")
        password = os.getenv("DB_PASS", "R6%40#Siege")
        database = os.getenv("DB_NAME", "sales_data_pipeline")
        host = os.getenv("DB_HOST", "localhost")

        # Create SQLAlchemy engine
        engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}/{database}")
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

        # Perform transformations
        df['sale_date'] = pd.to_datetime(df['sale_date'])
        df['calculated_total'] = df['quantity'] * df['price']
        mismatched_rows = df[df['total'] != df['calculated_total']]
        if not mismatched_rows.empty:
            logging.warning("Mismatched rows found during 'total' validation")
            logging.info(f"Mismatched rows:\n{mismatched_rows}")

        logging.info("Data transformations completed")

        # Save the transformed data to a CSV file
        output_path = '../data/transformed_sales_data.csv'
        os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure output directory exists
        df.to_csv(output_path, index=False)
        logging.info(f"Transformed data saved to {output_path}")

        print("ETL process completed successfully!")
        logging.info("ETL process completed successfully")

    except Exception as e:
        logging.error(f"Error during ETL: {e}")
        print(f"ETL process failed: {e}")

if __name__ == "__main__":
    run_etl()
