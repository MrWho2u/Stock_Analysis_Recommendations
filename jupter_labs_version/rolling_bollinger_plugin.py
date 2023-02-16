import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()
from datetime import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go
import hvplot.pandas

def boiler_table(stock_df,ticker):
    rolls = (10, 22, 42, 63, 126)
    dfs_names = ('15 day', '30 day', '60 day', '90 day', '180 day')
    dfs = pd.DataFrame()
    
    for i,n in zip(rolls, dfs_names):
        temp_stock_df = stock_df
        # Calculate the rolling mean and standard deviation
        temp_stock_df['Rolling Mean'] = temp_stock_df['Close'].rolling(window=i).mean()
        temp_stock_df['Rolling Std'] = temp_stock_df['Close'].rolling(window=i).std()
        
        # Create a new dataframe with the close price, rolling mean, and rolling standard deviation
        rolling_stock_df = stock_df[['Close', 'Rolling Mean', 'Rolling Std']]
    
        # Calculate the upper and lower Bollinger Bands
        upper_band = stock_df['Rolling Mean'] + 2 * stock_df['Rolling Std']
        lower_band = stock_df['Rolling Mean'] - 2 * stock_df['Rolling Std']
        
        temp_boil_df = pd.concat([stock_df['Close'], upper_band, lower_band], axis=1)
        temp_boil_df.columns = ['Close', 'Upper Band', 'Lower Band']
        end = dt.date.today()
        start= end - dt.timedelta(days=60)
        temp_boil_df = temp_boil_df[start:end]
        temp_boil_df["Rolling Bolling Rang"]=n
        dfs = dfs.append(temp_boil_df)
    
    bolling_graph = dfs.hvplot.line(title = f'Rolling Bollinger Bands For {ticker}', groupby="Rolling Bolling Rang")
        
    return bolling_graph