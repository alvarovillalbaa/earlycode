from this import d
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bs4 import BeautifulSoup  # To pull data out of HTML and XML files
import requests
import json
import time
import ssl

st.set_option("deprecation.showPyplotGlobalUse", False)

# To avoid 'Invalid Certification' Problem
ssl._create_default_https_context = ssl._create_unverified_context

# WE'LL USE CAMELCASE IN VARIABLES(ALVARO VILLABA'S STANDARDS)

# Expand content to full width
st.set_page_config(layout="wide")

image = Image.open("cryptoheader.jpg")
st.image(image, width=600)

st.title("Crypto Currency Surge X Web App")
st.markdown(
    """
            This Web App retrieves cryptocurrency prices for the top 100 cryptocurrency from **CoinMarketCap**!
            """
)

# About. We'll use a bar to be expanded this time (instead of having it fixed)
expander_bar = st.expander("About")
expander_bar.markdown(
    """
                      * **Python Libraries:** base64, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
                      * **Data Source:** [CoinMarketCap](https://coinmarketcap.com/).
                      """
)

# Divide page to 3 columns (column1 = sidebar, column2 and column3 = page contents)
column1 = st.sidebar
column2, column3 = st.columns((2, 1))  # 2, 1 is the size ratio of the columns (2:1)

column1.header("Features Filter")
currencyPriceUnit = column1.selectbox("Select currency:", ("USD", "EUR", "BTC", "ETH"))

# Here we'll manage another way of making web scraping by requesting to json files. Similar to API calls on other projects.
@st.cache
def loadStats():
    cmc = requests.get("https://coinmarketcap.com")
    soup = BeautifulSoup(cmc.content, "html.parser")

    data = soup.find(
        "script", id="__NEXT_DATA__", type="application/json"
    )  # In order to see what we're looking for: Webpage > Dev Tools > Elements. Then we'll find the dictionaries on HTML elements
    coins = {}  # Creates a dictionary of coins
    coinData = json.loads(data.contents[0])
    listings = coinData["props"]["initialState"]["cryptocurrency"]["listingLatest"][
        "data"
    ]
    for i in listings:
        coins[str(i["id"])] = i["slug"]

    coinName = []
    coinSymbol = []
    marketCap = []
    percentChange1h = []
    percentChange24h = []
    percentChange7d = []
    price = []
    volume24h = []
    # I also want the mcap/volume ratio

    for i in listings:
        coinName.append(i["slug"])
        coinSymbol.append(i["symbol"])
        price.append(i["quote"][currencyPriceUnit]["price"])
        percentChange1h.append(i["quote"][currencyPriceUnit]["percentChange1h"])
        percentChange24h.append(i["quote"][currencyPriceUnit]["percentChange24"])
        percentChange7d.append(i["quote"][currencyPriceUnit]["percentChange7d"])
        marketCap.append(i["quote"][currencyPriceUnit]["marketCap"])
        volume24h.append(i["quote"][currencyPriceUnit]["volume24h"])

    # Cleaner code this way, but could've made it one-liner
    df = pd.DataFrame(
        columns=[
            "coinName",
            "coinSymbol",
            "price",
            "marketCap",
            "percentChange1h",
            "percentChange24h",
            "percentChange7d",
            "volume24h",
        ]
    )
    df["coinName"] = coinName
    df["coinSymbol"] = coinSymbol
    df["price"] = price
    df["marketCap"] = marketCap
    df["percentChange1h"] = percentChange1h
    df["percentChange24h"] = percentChange24h
    df["percentChange7d"] = percentChange7d
    df["volume24h"] = volume24h
    return df


df = loadStats()

# Sidebar - Cryptocurrency selection
sortedCoin = sorted(df["coinSymbol"])  # We want to sort it by marketCap
selectedCoin = column1.multiselect("CRYPTOCURRENCY", sortedCoin, sortedCoin[:10])

# Filtering Data
df_selectedCoin = df[(df["coinSymbol"].isin(selectedCoin))]

# Sidebar - Number of Coins to display
numCoin = column1.slider("Display Top N Coins", 1, 100, 200)
df_coins = df_selectedCoin[:numCoin]

# Sidebar - Percentage change TimeFrame
percentTimeFrame = column1.selectbox("Percent Change Time Frame", ["1", "24", "7d"])
percentDictionary = {
    "1h": "percentChange1h",
    "24h": "percentChange24h",
    "7d": "percentChange7d",
}
selectedPercentTimeFrame = percentDictionary[percentTimeFrame]

# Sidebar - Sorting Values
sortValues = column1.selectbox("Sort Values", ["Yes", "No"])

# Column 2 - Titles and file download
column2.subheader("Price Data of Selected Cryptocurency")
column2.write(
    "Data Dimension: "
    + str(df_selectedCoin.shape[0])
    + " rows and "
    + str(df_selectedCoin.shape[1])
    + " columns."
)

column2.dataframe(df_coins)  # Difference between dataframe and DataFrame??

# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def fileDownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <---> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
    return href


column2.markdown(fileDownload(df_selectedCoin), unsafe_allow_html=True)

# Bar Plot of % Price Change
column2.subheader("Table of % Price Change")
df_change = pd.concat(
    [
        df_coins.coinSymbol,
        df_coins.percentChange1h,
        df_coins.percentChange24h,
        df_coins.percentChange7d,
    ],
    axis=1,
)  # axis=1 == axis="columns" == vertical axis
df_change = df_change.set_index("coinSymbol")
df_change["positivePercentChange1h"] = df_change["percentChange1h"] > 0
df_change["positivePercentChange24h"] = df_change["percentChange24h"] > 0
df_change["positivePercentChange7d"] = df_change["percentChange7d"] > 0
column2.dataframe(df_change)

# Conditional creation of Bar Plot (timeframe)
# Depends on the selected timeframe...
column3.subheader("Bar Plot of % Price Change")

if percentTimeFrame == "1h":
    if sortValues == "Yes":
        df_change = df_change.sort_values(by=["percentChange1h"])
    column3.write("*1 Hour Period*")
    plt.figure(figsize=(3, 20))
    plt.subplots_adjust(top=1, bottom=0)
    df_change["percentChange1h"].plot(
        kind="barh",
        color=df_change.positivePercentChange1h.map({True: "green", False: "red"}),
    )
    column3.pyplot(plt)

elif percentTimeFrame == "24h":
    if sortValues == "Yes":
        df_change = df_change.sort_values(by=["percentChange24d"])
    column3.write("*24 Hours Period*")
    plt.figure(figsize=(3, 20))
    plt.subplots_adjust(top=1, bottom=0)
    df_change["percentChange24h"].plot(
        kind="barh",
        color=df_change.positivePercentChange24h.map({True: "green", False: "red"}),
    )
    column3.pyplot(plt)

else:
    if sortValues == "Yes":
        df_change = df_change.sort_values(by=["percentChange7d"])
    column3.write("*7 Days Period*")
    plt.figure(figsize=(3, 20))
    plt.subplots_adjust(top=1, bottom=0)
    df_change["percentChange7d"].plot(
        kind="barh",
        color=df_change.positivePercentChange7d.map({True: "green", False: "red"}),
    )
    column3.pyplot(plt)
