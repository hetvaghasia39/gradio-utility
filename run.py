import gradio as gr
import pyodbc
import pandas as pd
from datetime import datetime

def fetch_filtered_data(start_date, end_date):
    try:
        # SQL Server connection parameters
        conn_str = (
            "Driver={SQL Server};"
            "Server=YOUR_SERVER_NAME;"
            "Database=YOUR_DATABASE_NAME;"
            "Trusted_Connection=yes;"  # For Windows authentication
            # For SQL authentication, use:
            # "UID=your_username;"
            # "PWD=your_password;"
        )
        
        # Convert string dates to datetime objects
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
        # Connect to database
        conn = pyodbc.connect(conn_str)
        
        # Example query - modify according to your table structure
        query = """
            SELECT *
            FROM YourTable
            WHERE DateColumn >= ? AND DateColumn <= ?
            ORDER BY DateColumn
        """
        
        # Execute query with parameters
        df = pd.read_sql(query, conn, params=[start_date, end_date])
        
        # Close connection
        conn.close()
        
        # Format the dates in the dataframe for display
        date_columns = df.select_dtypes(include=['datetime64']).columns
        for col in date_columns:
            df[col] = df[col].dt.strftime('%Y-%m-%d')
            
        return df
    
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
def filter_data(start_date, end_date):
    if start_date > end_date:
        return "Error: Start date must be before or equal to end date"
    
    result = fetch_filtered_data(start_date, end_date)
    
    if isinstance(result, pd.DataFrame):
        return result.to_html()
    else:
        return result


# Create dummy data
dummy_data = [
    {"date": "2024-01-01", "sales": 1500, "items": 10},
    {"date": "2024-01-05", "sales": 2000, "items": 15},
    {"date": "2024-01-10", "sales": 1800, "items": 12},
    {"date": "2024-01-15", "sales": 2200, "items": 18},
    {"date": "2024-01-20", "sales": 1900, "items": 14},
    {"date": "2024-01-25", "sales": 2100, "items": 16},
    {"date": "2024-01-30", "sales": 2300, "items": 20}
]

# Convert to DataFrame
df = pd.DataFrame(dummy_data)

def filter_dates(start_date, end_date):
    """
    Filter function that returns data between start_date and end_date
    """
    filtered_df = df[
        (df['date'] >= start_date) & 
        (df['date'] <= end_date)
    ]
    return filtered_df.to_html(index=False)

# Create the Gradio interface
demo = gr.Interface(
    fn=filter_dates,  
    inputs=[
        gr.Textbox(label="Start Date (YYYY-MM-DD)", value="2024-01-01"),
        gr.Textbox(label="End Date (YYYY-MM-DD)", value="2024-01-20")
    ],
    outputs=gr.HTML(label="Filtered Results")
)

if __name__ == "__main__":
    demo.launch()