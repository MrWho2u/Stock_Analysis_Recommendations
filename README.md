# Stock_Analysis_Recommendations
**The code will assign a recommend buy/hold/sell based on stock movements and user entered data points.**

## Rolling Standard Deviation Plotting Tool
**This is a tool to visualize the rolling standard deviation of a stock's price over a given date range and with a specified window size. The stock's price data is obtained from Yahoo Finance and the mean rolling standard deviation is calculated and plotted using Matplotlib.**

### Prerequisites
**The following libraries must be installed:**
datetime
pandas
pandas_datareader
yfinance
matplotlib

### Usage
1. Clone the repository to your local machine
2. Open the terminal and navigate to the folder where the script is located
3. Run the following command: python3 standard_deviation_plot.py
4. Select a stock from the list of predefined options
5. Enter the symbol of the stock you want to plot
6. Choose a window size from 4 options
7. The mean rolling standard deviation of the chosen stock over the date range will be plotted in a line graph

### Functionality
The main functionality of the tool is defined in the main function and executed when the script is run. The main function does the following:

Sets the start and end dates between today and 30 years ago
Allows the user to select a stock from a predefined list
Allows the user to choose a window size from a predefined list
Calls the plot_rolling_std function and passes in the chosen stock symbol, date range, and window size as arguments.

The plot_rolling_std function is responsible for the following:

Obtains the price data of the chosen stock and the S&P 500 from Yahoo Finance
Calculates the mean rolling standard deviation of the chosen stock and plots it on a line graph using Matplotlib

### Conclusion
This tool provides a simple way to visualize the rolling standard deviation of a stock's price and can be useful for stock market analysis. It can be easily extended to plot other stock market indicators or to analyze multiple stocks at once.

