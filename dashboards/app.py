from flask import Flask, render_template, jsonify
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the transformed data
data_file = '../data/transformed_sales_data.csv'

@app.route('/')
def home():
    """Homepage displaying sales summary."""
    # Load data
    try:
        data = pd.read_csv(data_file)
        total_sales = data['Sales'].sum()
        total_quantity = data['Quantity'].sum()
        regions = data['Region'].nunique()
        products = data['Product'].nunique()
    except Exception as e:
        return f"Error loading data: {e}"

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
        data = pd.read_csv(data_file)
        return jsonify(data.to_dict(orient='records'))
    except Exception as e:
        return {"error": f"Error loading data: {e}"}, 500

if __name__ == '__main__':
    app.run(debug=True)
