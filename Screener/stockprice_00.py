import yfinance as yf
import streamlit as st
import pandas as pd
import string

st.write(
    """
    # Simple Stock Price App
    We'll use a powerful library called streamlit to create simple Data Science projects.\nThis one is about reflecting the stock prices of any company based on the user input.\n
    
    Shown are the stock **closing price** and **volume** of TESLA!\n"""
)

# The main difference with the other stockscreener is the simplicity of the code with the built-in resources of te library
# To initialize it: streamlit run stockprice.py

# tickerSymbol = input("Introduce the Ticker Symbol: ")
# print("We are going to set time frame, starting and end period.\n")
# period = input("What time frame? ")

# startingDay = int(input("Starting day: "))
# startingMonth = int(input("Starting month: "))
# startingYear = int(input("Starting year: "))
# start = str(startingYear) + "-" + str(startingMonth) + "-" + str(startingDay)

# endingDay = int(input("Ending day: "))
# endingMonth = int(input("Ending month: "))
# endingYear = int(input("Ending year: "))
# end = str(endingYear) + "-" + str(endingMonth) + "-" + str(endingDay)

tickerSymbol = "TSLA"

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period="1d", start="2018-2-27", end="2022-3-10")

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
