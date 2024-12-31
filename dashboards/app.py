from flask import Flask, render_template, jsonify
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
DATA_FILE = os.getenv("DATA_FILE", "../data/transformed_sales_data.csv")

# Utility function to load and validate data
def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")
    data = pd.read_csv(file_path)
    
    # Ensure necessary columns exist
    required_columns = ['total_sales', 'quantity', 'region_name', 'product_name']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    return data

@app.route('/')
def home():
    """Homepage displaying sales summary."""
    try:
        data = load_data(DATA_FILE)
        total_sales = data['total_sales'].sum()
        total_quantity = data['quantity'].sum()
        regions = data['region_name'].nunique()
        products = data['product_name'].nunique()
    except Exception as e:
        app.logger.error(f"Error loading data: {e}")
        return render_template('error.html', message="Unable to load sales data. Please try again later.")

    return render_template(
        'dashboard.html',
        total_sales=total_sales,
        total_quantity=total_quantity,
        regions=regions,
        products=products
    )

@app.route('/api/sales')
def api_sales():
    """API endpoint to serve sales data as JSON."""
    try:
        data = load_data(DATA_FILE)
        return jsonify(data.to_dict(orient='records'))
    except Exception as e:
        app.logger.error(f"Error loading data: {e}")
        return {"error": "Unable to load sales data."}, 500

if __name__ == '__main__':
    app.run(debug=True)
