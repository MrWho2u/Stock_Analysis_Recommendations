import streamlit as st
import pandas as pd
import numpy as np

#Title and Background options
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
load_css("custom.css")





st.title("Financial Advisor")


ticker = st.sidebar.text_input("Enter stock ticker symbol:")
investment = st.sidebar.text_input("Enter the investment amount:")
time_frame = st.sidebar.selectbox("Select the time frame:", ["Days", "Months", "Years"])
holding_period_value = st.sidebar.text_input("Enter the holding period value:")
risk = st.sidebar.slider("Enter the risk level (1-10):", 1, 10)



# Display the results
if ticker and holding_period_value and investment:
    st.write("Investing ${} in {} for {} {} with risk level {}".format(investment, ticker, holding_period_value, time_frame, risk))
    st.write("Expected returns: Graphs")
