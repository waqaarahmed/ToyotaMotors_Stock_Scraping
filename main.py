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
