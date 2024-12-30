# Sales Data Pipeline and Dashboard

## Project Overview
This project demonstrates a real-time data pipeline for analyzing sales data. The pipeline ingests data using Kafka, processes it using Python (Pandas), stores it in MySQL, and visualizes it via dashboards using Dash and Flask.

## Features
- Real-time data ingestion and processing.
- Interactive and static dashboards for visual insights.
- Download filtered data directly from the dashboard.
- Deployed using Railway for easy access.

## Tech Stack
- **Data Ingestion**: Kafka
- **Data Processing**: Python (Pandas, NumPy)
- **Storage**: MySQL
- **Visualization**: Dash (Plotly) and Flask
- **Deployment**: Railway


## Project Structure
 ├── data_pipeline/ │ ├── kafka_producer.py │ ├── kafka_consumer.py │ └── transformations.py ├── dashboards/ │ ├── dashboard.py │ ├── app.py │ └── templates/ │ └── dashboard.html ├── data/ │ ├── raw_sales_data.csv │ ├── transformed_sales_data.csv │ └── sample_data.json ├── logs/ │ └── kafka_consumer.log ├── README.md ├── requirements.txt └── .env


## Setup Instructions

### Prerequisites
1. **Install Python**: Python 3.8 or higher is recommended.
2. **Install MySQL**: Set up a MySQL server.
3. **Install Kafka**: Set up a local or remote Kafka server.
4. **Railway Account**: For deployment.

### Steps to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/sales-data-pipeline.git
   cd sales-data-pipeline

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Set Up Environment Variables: Create a .env file in the project root and add your MySQL credentials**:
   ```makefile
   DB_HOST=<your-database-host>
   DB_USER=<your-database-user>
   DB_PASSWORD=<your-database-password>
   DB_NAME=<your-database-name>

4. **Run the Kafka Producer: Start producing sample data**:
   ```bash
   python data_pipeline/kafka_producer.py

5. **Run the Kafka Consumer: Start consuming and storing data in MySQL**:
   ```bash
   python data_pipeline/kafka_consumer.py

6. **Launch the Dash Dashboard**:
   ```bash
   python dashboards/dashboard.py

7. **launch the Flask Dashboard**:
   ```bash
   python dashboards/app.py

8. **Access the Dashboards**:
   Dash Dashboard: http://127.0.0.1:8050
   Flask Dashboard: http://127.0.0.1:5000


## Deployment
The project is deployed using Railway. You can access the deployed app via the Railway-generated URL.


## Contributing
Feel free to fork the repository and create pull requests for improvements.


## License
This project is licensed under the MIT License.

MIT License

Copyright (c) 2024 The-morning-star23

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

