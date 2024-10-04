
# Stock Price & Revenue Data Visualization Tool

This Python project fetches and visualizes historical stock prices and revenue data for major companies, such as Toyota and Honda, using `yfinance`, web scraping, and `Plotly` for graphical representation. The tool also displays the stock and revenue data in a full-screen, scrollable window using `Tkinter`.

## Features

- **Stock Data Fetching**: Fetch historical stock data for companies using the `yfinance` API.
- **Web Scraping Revenue Data**: Extract quarterly revenue data from websites (e.g., Macrotrends) using `BeautifulSoup` and `requests`.
- **Graphical Visualization**: Plot stock prices and revenue data using `Plotly` subplots.
- **Full-Screen Data View**: Display fetched stock and revenue data in full-screen scrollable windows using `Tkinter`.

## Requirements

To run the project, you'll need the following Python libraries:

```bash
pip install pandas yfinance requests beautifulsoup4 plotly tkinter
```

## How to Use

1. **Stock Data Fetching**: 
   - The script fetches historical stock price data for Toyota (`TM`) and Honda (`HMC`) using `yfinance`.
   - You can modify the stock tickers to retrieve data for other companies.

2. **Revenue Data Extraction**: 
   - The script scrapes quarterly revenue data from Macrotrends by providing the URL and the table text identifier.
   - The revenue data is cleaned before being displayed and plotted.

3. **Data Visualization**: 
   - Use the `plot_graph()` function to plot two subplots: one for the historical share price and one for revenue.

4. **Display Data in a Full-Screen Window**: 
   - The `show_data_in_window()` function creates a full-screen window to display data in a scrollable text widget. Press `Esc` to exit full-screen mode.

## Example

The example code included in the script demonstrates fetching and visualizing data for Toyota and Honda:

```python
# Fetch stock and revenue data for Toyota
toyota_data = yf.Ticker('TM').history(period='max').reset_index()
toyota_revenue = extract_revenue_data('https://www.macrotrends.net/stocks/charts/TM/toyota/revenue', 'Toyota Quarterly Revenue')

# Clean and display data
show_data_in_window("Toyota Motors Stock Data", toyota_data)
show_data_in_window("Toyota Motors Revenue Data", toyota_revenue)

# Plot data
plot_graph(toyota_data, toyota_revenue, 'Toyota Motors Historical Share Price & Revenue')
```

You can modify the URLs and stock tickers to fetch and visualize data for other companies.

## Functions

- `plot_graph(stock_data, revenue_data, stock)`: Plots historical stock prices and revenue using Plotly.
- `extract_revenue_data(url, table_text)`: Scrapes revenue data from the given URL.
- `show_data_in_window(title, data)`: Displays data in a scrollable full-screen Tkinter window.

## Dependencies

The project relies on several libraries:
- `pandas`: For data manipulation.
- `yfinance`: To fetch stock price data.
- `requests` and `BeautifulSoup`: For web scraping.
- `Plotly`: For interactive data visualization.
- `Tkinter`: For creating GUI windows to display data.

## License

This project is licensed under the MIT License.
