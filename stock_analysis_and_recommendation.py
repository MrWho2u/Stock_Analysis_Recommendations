import requests
import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()
from datetime import datetime
from dateutil.relativedelta import relativedelta
import hvplot.pandas
from warnings import filterwarnings
filterwarnings("ignore")
import fire


from variables_plugin import (get_stock_name, question_ask,)
from stock_tables_plugin import (stock_analysis_tables,)
from monte_carlo_plugin import (monte_carlo_simulation,)
from metric_results_plugin import (calculate_metrics,)
from rolling_bollinger_plugin import (boiler_table,)

def run():
    #get stock ticker, holding time and holding unit
    ticker, hold_time, hold_unit, req_return = question_ask()
    #get table data for functions
    rolling_stock_df, bollinger_df, stock_return_df, spy_return_df, stock_spy_return_df, stock_df, spy_df = stock_analysis_tables(ticker)
    # run monte carlo simulation to test results
    monte_carlo_return_table_df, mean, lower_bound, upper_bound, avg_cum_stock_return_df, avg_cum_spy_return_df = monte_carlo_simulation(ticker, hold_unit, hold_time, stock_df, spy_df)
    # analize all the data and provide results
    stock_sharpe_ratio, stock_sortino_ratio, bench_sharpe_ratio, bench_sortino_ratio, ratio_lang_final, sharpe_comp, return_lang, boiler_lang, final_lang = calculate_metrics(stock_return_df, req_return, ticker, spy_return_df, hold_unit, hold_time, avg_cum_stock_return_df, avg_cum_spy_return_df, bollinger_df)
    # create an adaptive bollinger band graph
    bollinger_graph = boiler_table(stock_df,ticker)
    
    #create Monte Carlo Graph
    monte_carlo_graph = monte_carlo_return_table_df.hvplot.line(title = f"Average {hold_time} {hold_unit} Cumulative Return Monte Carlo Simulation (1,000 simulations)")
    
    return display(ratio_lang_final), display(bollinger_graph), display(boiler_lang), display(monte_carlo_graph), display(return_lang), print(), display(final_lang)

# Entry point for the application. Initiates the run() function.
if __name__ == "__main__":
    run()