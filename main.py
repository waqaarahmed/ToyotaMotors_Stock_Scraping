import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import tkinter as tk
from tkinter import scrolledtext

def plot_graph(stock_data, revenue_data, stock):
    """Function to plot historical share price and revenue data"""
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        subplot_titles=("Historical Share Price ($)", "Historical Revenue ($)"), 
                        vertical_spacing=0.5)
    
    # Plotting Share Price
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data['Date'], infer_datetime_format=True), 
                             y=stock_data['Close'].astype("float"), name="Share Price"), row=1, col=1)
    
    # Plotting Revenue
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data['Date'], infer_datetime_format=True), 
                             y=revenue_data['Revenue'].astype("float"), name="Revenue"), row=2, col=1)
    
    # Updating axes and layout
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($ Millions)", row=2, col=1)
    fig.update_layout(showlegend=False, height=1000, title=stock, xaxis_rangeslider_visible=True)
    fig.show()

def extract_revenue_data(url, table_text):
    """Function to extract revenue data from a given URL and table text."""
    # Using requests to download the webpage
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html5lib')

    # Find the table with the given text in it
    tables = soup.find_all('table')
    table_index = None

    for index, table in enumerate(tables):
        if table_text in str(table):
            table_index = index
            break

    # Extract revenue data if table found
    revenue_data = pd.DataFrame(columns=["Date", "Revenue"])
    if table_index is not None:
        table_body = tables[table_index].find("tbody")
        if table_body:
            rows = table_body.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if cols:
                    date = cols[0].text
                    revenue = cols[1].text.replace("$", "").replace(",", "")
                    revenue_data = pd.concat([revenue_data, pd.DataFrame({'Date': [date], 'Revenue': [revenue]})], ignore_index=True)
    return revenue_data
