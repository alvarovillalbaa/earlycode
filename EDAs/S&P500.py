import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import base64
import yfinance as yf
import ssl

# AS WE ARE TRYING TO FETCH 505 CHARTS, IT WILL TAKE QUITE LONG TO LOAD

st.set_option("deprecation.showPyplotGlobalUse", False)

# To avoid 'Invalid Certification' Problem
ssl._create_default_https_context = ssl._create_unverified_context

# Most of the things on EDAs are already explained on basketball.py so we'll limit on new information

st.title("S&P 500 Web App")

st.markdown(
    """
            This web app retrieves the list of the **S&P 500** from wikipedia.com and its corresponding **stock closing price** (year-to-date)!
            * **Python libraries: ** base64, pandas streamlit, numpy, matplot, yfinance
            * **Data Source: ** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
            """
)

st.sidebar.header("Features Filter")

# Web Scraping of S&P 500 data


@st.cache
def loadStats():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html = pd.read_html(url, header=0)  # So that it's not put as a header
    df = html[0]
    return df


df = loadStats()
sector = df.groupby("GICS Sector")

# Sidebar - Sector Selection
sortedUniqueSector = sorted(df["GICS Sector"].unique())
selectedSector = st.sidebar.multiselect(
    "SECTOR", sortedUniqueSector, sortedUniqueSector
)

# Filtering Data
df_selectedSector = df[df["GICS Sector"].isin(selectedSector)]

st.header("Companies in Selected Sector")
st.write(
    "Data Dimension: "
    + str(df_selectedSector.shape[0])
    + " rows and "
    + str(df_selectedSector.shape[1])
    + " columns."
)
st.dataframe(df_selectedSector)

# Downloading S&P 500 Data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def fileDownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <---> bytes conversions
    href = f"<a href='data:file/csv;base64,{b64}' download='SP500.csv'>Download CSV File</a>"
    return href


st.markdown(fileDownload(df_selectedSector), unsafe_allow_html=True)

# Implementing financials to our data. https://pypi.org/project/yfinance/

# We could ask for user input for parameters personalisation
data = yf.download(  # or pdr.get_data_yahoo(...)
    tickers=list(df_selectedSector.Symbol),
    period="max",  # We use period instead of start/end. Valid periods: 1d, 5d, 1mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    interval="1wk",  # default is 1mo. Valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    group_by="ticker",
    auto_adjust=True,  # Adjust all OHLC automatically. Default is False
    prepost=True,  # Download pre/post market hours data. Default is False
    threads=True,  # Use threads for mass downloading? (True/False/Integer). Default is True
    proxy=None,  # proxy URL scheme use when downloading. Default is None. A proxy acts as a gateway between the user and the internet
)

# Plot Closing Price of Tickers Symbols
def pricePlot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df["Date"] = df.index
    plt.fill_between(
        df.Date, df.Close, color="cadetblue", alpha=0.24
    )  # alpha determines its opacity
    plt.plot(df.Date, df.Close, color="cadetblue", alpha=0.76)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight="bold")
    plt.xlabel("Date", fontweight="bold")
    plt.ylabel("Closing Price", fontweight="bold")
    return st.pyplot()


numCompanies = st.sidebar.slider("Number of Companies", 1, 506)

if st.button("Show Charts"):
    st.header("Stock Closing Price")
    for i in list(df_selectedSector.Symbol)[:numCompanies]:
        pricePlot(i)
