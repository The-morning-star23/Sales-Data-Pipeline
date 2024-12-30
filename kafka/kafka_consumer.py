import logging
from kafka import KafkaConsumer
import pandas as pd
from sqlalchemy import create_engine

# Set up logging
logging.basicConfig(
    filename='logs/kafka_consumer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # Kafka Consumer
    consumer = KafkaConsumer(
        'sales',
        bootstrap_servers='localhost:9092',
        group_id='sales_group',
        auto_offset_reset='earliest'
    )

    # MySQL connection
    engine = create_engine('mysql+mysqlconnector://username:password@localhost/sales_data')

    for message in consumer:
        logging.info(f"Received message: {message.value}")
        data = pd.read_json(message.value)
        data.to_sql('sales_raw', con=engine, if_exists='append', index=False)
        logging.info("Data inserted into MySQL")

except Exception as e:
    logging.error(f"Error occurred: {e}")
