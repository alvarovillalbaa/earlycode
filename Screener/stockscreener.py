from notes import ameritrade
import requests, time, re, os  # Requests are used to get API information. re = regular expressions
import pandas as pd  # Data Science w/Python: return
import pickle as pickle

url = "https://api.tdameritrade.com/v1/instruments"

df = pd.read_excel("company_list.xlsx")
symbols = df[
    "Symbol"
].values.tolist()  # creates a column which takes the values to a list
# All the symbols from NASDAQ and SP is 5456

start = 0
end = 500  # Means we can check 500 at a time
files = []  # To track, extract and merge the pkl files generated
while start < len(symbols):
    tickers = symbols[start:end]

    payload = {
        "apikey": ameritrade,
        "symbol": tickers,
        "projection": "fundamental",
    }  # dictionary of what we want to access
    # We should be able to display any symbol we want without actually gettin into code
    # In python: variables are implicitly declared once it has an assigned value

    results = requests.get(url, params=payload)
    # We have to unpack the json dictionary
    data = results.json()
    f_name = (
        time.asctime() + ".pkl"
    )  # Pickle serializes and deserializes object structures(objects to bytes)
    # f_name = re.sub('[ :], '_', f_name) for WINDOWS(not recognised if not put)
    files.append(f_name)
    with open(f_name, "wb") as f:
        pkl.dump(data, f)  # To save the data from the API to a pickle(similar to json)

    start = end  # It's an iteration to avoid extra code after the loop
    end += 500
    time.sleep(1)  # waits for time execution for some seconds

# We need to unpack the things we want from the dictionary as a dataframe
data = []

for f in files:
    with open(f, "rb") as file:
        info = pkl.load(file)
    tickers = list(info)
    points = [
        "symbol",
        "high52",
        "low52",
        "dividendYield",
        "dividendDate",
        "peRatio",
        "quickRatio",
        "interestCoverage",
        "shortIntToFloat",
        "revChangeYear",
        "vol1DayAvg",
        "marketCap",
        "totalDebtToEquity",
    ]
    for ticker in tickers:
        tick = []
        for point in points:
            tick.append(info[ticker]["fundamental"][point])
        data.append(tick)

    os.remove(
        file
    )  # Makes your system overrun with files that build up troughout the day

points = [
    "Symbol",
    "52-W High",
    "52-W Low",
    "Dividend",
    "Dividend Date",
    "PE",
    "Quick Ratio",
    "Interest Coverage",
    "Short Interest",
    "Yearly Revenue Change",
    "Average Daily Volume",
    "MCAP",
    "Debt/Equity",
]  # We are renaming the wanted values

df_results = pd.DataFrame(data, columns=points)

# Next part is filtering the tickets depending on what the user want
# We can make a user input interface to let the executor choose a determined value of anything(for next project: full screener)
df_best = df_results[df_results["PE"] > 1]
