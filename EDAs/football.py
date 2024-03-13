import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import ssl

# To avoid 'Invalid Certification' Problem
ssl._create_default_https_context = ssl._create_unverified_context

st.set_option("deprecation.showPyplotGlobalUse", False)


# seaborn is a very strong library for statistical data visualization
# We will use Camel Case notation instead of snake_case

# Alternative to """# for titles
st.title("NFL Football Stats Explorer")

st.markdown(
    """
            Website App to perform webscraping of NFL player stats data!
            * **Python libraries:** base64, pandas, streamlit
            * ** Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
            """
)
# Used as Github to make it a clickable Data source
# * ** makes a bulleted bold text

# To make a User Filter we can use sidebar
# It will have all filters selected by default
st.sidebar.header("Features Filter")
selectedYear = st.sidebar.selectbox(
    "YEAR", list(reversed(range(1995, 2022)))
)  # We reverse it to start with the latest year displayed as a list
# all of these data are stored on the fly demand upon clicking on the input parameters so nothing is stored loccally on the server side

# Web Scraping of NBA Player Stats
# This shows us that there's not always a need for API requests, but we can use web scraping instead. Only problem is that we don't depend on 'ourselves' for data update. However, this data page also has its own API
@st.cache  # Because everytime we change a parameter(e.g. year) it will be reseting data load, so @st.cache makes the second data load much quicker
def loadStats(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/rushing.htm"
    html = pd.read_html(
        url, header=0
    )  # To easily read the data as table inside the url
    df = html[0]
    row = df.drop(df[df.Age == "Age"].index)  # PROBLEM: Age does not exist
    row = row.fillna(0)
    playerStats = row.drop(
        ["Rk"], axis=1
    )  # Rk is redundant cause already provided with pandas
    return playerStats


# To analyse these redundances to remove we should first display them

playerStats = loadStats(selectedYear)

# Sidebar Team Selection
sortedUniqueTeam = sorted(
    playerStats.Tm.unique()
)  # Display unique values of team columns
selectedTeam = st.sidebar.multiselect(
    "TEAM", sortedUniqueTeam, sortedUniqueTeam[:3]
)  # To being able to select nultiple teams. We can make a slice in the third(default) argument. We just want to look at some teams

# Sidebar Position Selection
uniquePos = [
    "RB",
    "QB",
    "WR",
    "FB",
    "TE",
]  # No need to sort because it's not alphabetically-wise
selectedPos = st.sidebar.multiselect(
    "POSITION", uniquePos, uniquePos
)  # Third argument is to establish the default value(same in sortedUniqueTeam)

# Filtering data
df_selectedTeam = playerStats[
    (playerStats.Tm.isin(selectedTeam)) & (playerStats.Pos.isin(selectedPos))
]  # Boolean to check wether each element in the DataFrame is contained in values, then change its dimension on df if changed sidebar selection. Very strong tool for data filtering capability

st.header("Player Stats of Selected Team(s) and Position(s)")
st.write(
    "Data Dimension: "
    + str(df_selectedTeam.shape[0])
    + " rows and "
    + str(df_selectedTeam.shape[1])
    + " columns."
)  # Shape returns a tuple of integers which denote the lenght of the corresponding dimension
st.dataframe(df_selectedTeam)

# Download NBA Player Stats Data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
# To be able to create a downloadable file for the user through a linked text. We create the next function
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <---> conversions
    href = f"<a href='data:file/csv;base64,{b64}' download='playerstats.csv'>Download CSV File</a>"
    return href


# We can accommplish this thanks to the base64 library above. Encode it and decode it.

st.markdown(filedownload(df_selectedTeam), unsafe_allow_html=True)

# Intercorrelation Heatmap is a two dimensional plot which measures variables dependance amongst each other. Linear relationship between variables
if st.button("Intercorrelation Heatmap"):  # means if hit the button
    st.header("Intercorrelation Surge X Heatmap")
    df_selectedTeam.to_csv("output.csv", index=False)  # To save it as csv
    df = pd.read_csv("output.csv")  # Reads the saved csv

    # Combining numpy calculations with seaborn graphics to create heatmap (see documentation)
    correlation = df.corr()
    mask = np.zeros_like(correlation)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(correlation, mask=mask, vmax=1, square=True)

    st.pyplot()
