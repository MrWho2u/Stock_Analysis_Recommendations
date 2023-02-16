#import required libaries
import streamlit as st
import pandas as pd
import numpy as np
import requests
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()
from datetime import datetime
import matplotlib.pyplot as plt
from warnings import filterwarnings
filterwarnings("ignore")

# Grab functions for python files
from stream_modules.run_all import run
from stream_modules.ticker_checker_plugin import ( get_stock_name, question_ask,)
from stream_modules.stream_bollinger import boiler_table

#set up streamlit page
st.set_page_config(page_title="My Webpage", page_icon="tda", layout="wide")

#create a page header
with st. container():
    st.title("Stock Analyizer & Recommendation")
    st.write("Lets see how good your investment decisions are!")

#create the anslysis section
with st.container():
    st.write("---")
    #create a column for imputs and a column for results
    col1, col2 = st.columns([1,3],gap="medium")
    #column 1 used for entering inputs that will define the function
    with col1:
        st.subheader("First, let's get some information")
        ticker = st.text_input("Please enter a stock ticker",value="TSLA").upper()
        hold_unit = st.selectbox("What period do you want to hold this stock for?",('Years','Months','Days')).lower()
        hold_period = int(st.number_input(f"How many {hold_unit}?",min_value=1))
        req_return = float(st.number_input(f"What is your annulized required rate of return?",min_value=0.00))
        stock_name = question_ask(ticker)
        if stock_name[0:4].lower() == 'inva':
            st.write(f"You have selected {stock_name}")
        else:
            st.write(f"You have selected {stock_name} with a holding period of {hold_period} {hold_unit} and you are looking for a {req_return}% return.")
    
    #column 2 will display the results
    with col2:
        #run the main functions and obtain all the neede variables and language
        graph_area, ratio_lang_final, stock_df, boiler_lang, monte_carlo_return_table_df, return_lang, final_lang = run(ticker,hold_unit,hold_period,req_return)
        #display ratio analysis results
        with st.container():
            st.subheader(f"{ticker} Ratio Analysis")
            st.write(f"{ratio_lang_final}")
        #display bollinger band results
        with st.container():
            st.write("---")
            #allow user to select bolling band range
            st.subheader(f"{ticker} Bollering Band Results")
            range = int(st.selectbox("Bolling Band Rolling Period",(15,30,60,90,180)))
            #run function to get new table
            bollinger_graph = boiler_table(stock_df, ticker, range)
            bollinger_graph
            st.write(f"{boiler_lang}")
        #show monte carlo simulation results
        with st.container():
            st.write("---")
            st.subheader(f"{ticker} Monte Carlo Simulation Results")
            graph_area
            st.write(f"{return_lang}")
        #show final recommendation results
        with st.container():
            st.write("---")
            st.subheader(f"{ticker} Final Recommendation")
            st.write(f"{final_lang}")
