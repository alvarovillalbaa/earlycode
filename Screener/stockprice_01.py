import yfinance as yf
import streamlit as st
import pandas as pd
import string

st.write(
    """
    # Simple Stock Price App
    We'll use a powerful library called streamlit to create simple Data Science projects.\nThis one is about reflecting the stock prices of any company based on the user input.\n
    
    Shown are the stock **closing price** and **volume**!\n"""
)

# The main difference with the other stockscreener is the simplicity of the code with the built-in resources of te library
# To initialize it: streamlit run stockprice.py

tickerSymbol = st.text_input("Introduce the Ticker Symbol: ")
print("We are going to set time frame, starting and end period.\n")
period = st.text_input("What time frame? ")

startingDay = st.text_input("Starting day: ")
startingMonth = st.text_input("Starting month: ")
startingYear = st.text_input("Starting year: ")
start = startingYear + "-" + startingMonth + "-" + startingDay

endingDay = st.text_input("Ending day: ")
endingMonth = st.text_input("Ending month: ")
endingYear = st.text_input("Ending year: ")
end = endingYear + "-" + endingMonth + "-" + endingDay

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period, start, end)

st.write(
    """
         ## Closing Price
         """
)
st.line_chart(tickerDF.Close)
st.write(
    """
         ## Volume
         """
)
st.line_chart(tickerDF.Volume)
