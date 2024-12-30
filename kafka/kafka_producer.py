from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

products = ['Laptop', 'Mouse', 'Keyboard']
regions = ['North', 'South', 'East', 'West']

while True:
    sale = {
        'sale_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'product_name': random.choice(products),
        'region_name': random.choice(regions),
        'quantity': random.randint(1, 20),
        'price': round(random.uniform(100.0, 5000.0), 2),
        'total': None
    }
    sale['total'] = sale['quantity'] * sale['price']
    producer.send('sales_topic', sale)
    print(f"Produced: {sale}")
    time.sleep(1)
