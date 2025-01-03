import os
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dotenv import load_dotenv
import dash.exceptions

# Load environment variables
load_dotenv()

# Load transformed data
DATA_PATH = os.getenv("DATA_PATH", "data/transformed_sales_data.csv")
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Data file not found at {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# Ensure necessary columns exist
if 'month' not in df.columns:
    df['month'] = pd.to_datetime(df['sale_date']).dt.month

if 'total_sales' not in df.columns:
    df['total_sales'] = df['total']  # Assuming 'total' is the column to use

# Initialize Dash app
app = Dash(__name__)
app.title = "Enhanced Sales Dashboard"

# App layout
app.layout = html.Div([
    html.H1("Enhanced Sales Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Region:"),
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': region, 'value': region} for region in df['region_name'].unique()],
            value=df['region_name'].unique()[0] if not df.empty else None
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Select Category:"),
        dcc.Dropdown(
            id='category-dropdown',
            options=[{'label': category, 'value': category} for category in df['category'].unique()],
            value=df['category'].unique()[0] if not df.empty else None
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='sales-bar-chart'),
    dcc.Graph(id='sales-time-series'),

    html.Div([
        html.Button("Download Filtered Data", id="download-button"),
        dcc.Download(id="download-dataframe-csv")
    ], style={'textAlign': 'center', 'marginTop': '20px'})
])

# Callback for updating charts
@app.callback(
    [Output('sales-bar-chart', 'figure'),
     Output('sales-time-series', 'figure')],
    [Input('region-dropdown', 'value'),
     Input('category-dropdown', 'value')]
)
def update_dashboard(selected_region, selected_category):
    try:
        # Filter data
        filtered_df = df[(df['region_name'] == selected_region) & (df['category'] == selected_category)]

        # Handle empty filtered data
        if filtered_df.empty:
            raise dash.exceptions.PreventUpdate

        # Bar chart: Total sales by month
        bar_chart = {
            'data': [{
                'x': filtered_df['month'],
                'y': filtered_df['total_sales'],
                'type': 'bar',
                'name': selected_region
            }],
            'layout': {
                'title': f"Monthly Sales in {selected_region} ({selected_category})",
                'xaxis': {'title': 'Month (Jan-Dec)'},
                'yaxis': {'title': 'Total Sales'},
                'template': 'plotly_dark'
            }
        }

        # Time series: Sales trend
        time_series = {
            'data': [{
                'x': filtered_df['month'],
                'y': filtered_df['total_sales'],
                'type': 'line',
                'name': selected_region
            }],
            'layout': {
                'title': f"Sales Trend in {selected_region} ({selected_category})",
                'xaxis': {'title': 'Month (Jan-Dec)'},
                'yaxis': {'title': 'Total Sales'},
                'template': 'plotly_dark'
            }
        }

        return bar_chart, time_series

    except Exception as e:
        return {
            'data': [],
            'layout': {
                'title': 'No Data Available',
                'template': 'plotly_dark'
            }
        }, {
            'data': [],
            'layout': {
                'title': 'No Data Available',
                'template': 'plotly_dark'
            }
        }

# Callback for downloading filtered data
@app.callback(
    Output("download-dataframe-csv", "data"),
    [Input('region-dropdown', 'value'),
     Input('category-dropdown', 'value'),
     Input("download-button", "n_clicks")]
)
def download_filtered_data(selected_region, selected_category, n_clicks):
    if n_clicks is None:
        return dash.no_update
    filtered_df = df[(df['region_name'] == selected_region) & (df['category'] == selected_category)]
    return dcc.send_data_frame(filtered_df.to_csv, "filtered_sales_data.csv")

if __name__ == '__main__':
    # Run the app locally in development mode
    app.run_server(debug=True)
else:
    # Expose the Flask WSGI server for production
    server = app.server
