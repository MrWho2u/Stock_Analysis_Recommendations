import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()
from datetime import datetime
from dateutil.relativedelta import relativedelta

# The function has 5 outputs. Therefore, when you call the function, you must define 5 outputs.
# Example: rolling_stock_df, bollinger_df, stock_result_df, spy_result_df, stock_spy_return_df = stock_analysis_tables(10, 21)

def stock_analysis_tables (hold_period_years, window_size_days, ticker):
    end_date = dt.date.today()
    delta_months = hold_period_years * 12
    delta_days = hold_period_years * 365
    start_date = end_date - dt.timedelta(delta_days)
    relative_delta = round(window_size_days * 7 / 5 / 30)
    
    data_start_date = str(start_date - relativedelta(months=relative_delta))[0:10]

    stock_df = pdr.get_data_yahoo(ticker, start=data_start_date, end=end_date)
    spy = 'SPY'
    spy_df = pdr.get_data_yahoo(spy, start=data_start_date, end=end_date)
    
    # Calculate the rolling mean and standard deviation
    stock_df['Rolling Mean'] = stock_df['Close'].rolling(window=window_size).mean()
    stock_df['Rolling Std'] = stock_df['Close'].rolling(window=window_size).std()
    
    # Create a new dataframe with the close price, rolling mean, and rolling standard deviation
    rolling_stock_df = stock_df[['Close', 'Rolling Mean', 'Rolling Std']].loc[start_date:]
    
    # Calculate the upper and lower Bollinger Bands
    upper_band = stock_df['Rolling Mean'] + 2 * stock_df['Rolling Std']
    lower_band = stock_df['Rolling Mean'] - 2 * stock_df['Rolling Std']
    
    # Create a new dataframe with the stock close price, upper and lower Bollinger Bands
    bollinger_df = pd.concat([stock_df['Close'], upper_band, lower_band], axis=1).loc[start_date:]
    bollinger_df.columns = ['Close', 'Upper Band', 'Lower Band']
    
    # Calculate the daily stock return
    stock_return = stock_df['Close'].pct_change()
    
    # Create a new dataframe with the stock return
    stock_result_df = pd.DataFrame(stock_return).loc[start_date:]
    stock_result_df.columns = ['Stock Return']
    
    # Calculate the daily SPY return
    spy_return = spy_df['Close'].pct_change()
    
    # Create a new dataframe with the SPY return
    spy_result_df = pd.DataFrame(spy_return).loc[start_date:]
    spy_result_df.columns = ['SPY Return']
    
    # Combine the stock return and SPY return in one dataframe
    stock_spy_return_df = pd.concat([stock_result_df, spy_result_df], axis=1)
    
    return rolling_stock_df, bollinger_df, stock_result_df, spy_result_df, stock_spy_return_df