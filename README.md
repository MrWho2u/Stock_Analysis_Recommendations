# Stock_Analysis_Recommendations
**The code will assign a recommend buy/hold/sell based on stock movements and user entered data points.**

## Rolling Standard Deviation Plotting Tool
This is a tool to visualize the rolling standard deviation of a stock's price over a given date range and with a specified window size. The stock's price data is obtained from Yahoo Finance and the mean rolling standard deviation is calculated and plotted using Matplotlib.

### Prerequisites
The following libraries must be installed:
datetime
pandas
pandas_datareader
yfinance
matplotlib

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




## Monte Carlo Simulation
This is a Monte Carlo Simulation program which is used to forecast the future behavior of a stock based on past performance. It uses historical data to perform random simulations and estimate the potential future outcomes of an investment.

### Prerequisites
In order to run this program, you must have the following libraries installed:
datetime
pandas
pandas_datareader
yfinance
numpy
matplotlib

### Functionality
The program calculate the cumulative returns based on daily returns and initial investment.  

The program compare the average cumulative returns of selected stock and S&P 500

The program also uses the summarize_cumulative_return function to summarize the results of the Monte Carlo simulation by calculating the count, mean, standard deviation, minimum, 25th percentile, 50th percentile, 75th percentile, and maximum of the final cumulative returns. The summarize_cumulative_return function takes in one parameter: cumulative_returns.

The program uses the yfinance library to gather the historical data for the selected stock, and the numpy library to perform random simulations and statistical calculations. The program uses the matplotlib library to create the plots of the simulation results.

### Conclusion
Monte Carlo simulation is a powerful tool for predicting the future performance of a stock based on its historical returns. The simulation allows us to examine the distribution of possible future outcomes and estimate the likelihood of certain outcomes occurring. Based on the results, investors can make informed decisions about the future performance of the stock and assess the risk associated with their investment.

