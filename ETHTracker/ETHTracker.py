from time import time
from urllib import response
from requests import get
from matplotlib import pyplot as plt
from datetime import datetime

API_KEY = "AVQII4CRSAUWKJ7FPTHKPNBAHBZMT2QTFR"  # We can file this as a .env secret file so that people cannot see it
address = "0x73BCEb1Cd57C711feaC4224D062b0F6ff338501e"
BASE_URL = "https://api.etherscan.io/api"
ETHERVALUE = 10**18

# For account balance
# https://api.etherscan.io/api
# ?module=account
# &action=balance
# &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
# &tag=latest
# &apikey=YourApiKeyToken"""

# Normal transactions are the ones when interacting with an external aggent and an internal transaction is the one made thanks to the smart contracts


def make_api_url(
    module, action, address, **kwargs
):  # KWARGS are any other types of arguments like 'tag'(similar to a pointer)
    # used kwargs = {"tag": "latest", "x": 2} if we wanted to add any parameter
    url = (
        BASE_URL
        + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"
    )  # Thanks to this function we can call different APIs which use similar parameters and change them

    for key, value in kwargs.items():
        url += f"&{key}={value}"

    return url


def get_account_balance(address):
    get_balance_url = make_api_url(
        "acccount", "balance", address, tag="latest"
    )  # As we have declared KWARGS, tag is passed as argument
    response = get(get_balance_url)
    data = response.json()  # To create a json with all the keys and data

    value = int(data["result"]) / ETHERVALUE
    return value


# For 'Normal' Transactions
# https://api.etherscan.io/api
# ?module=account
# &action=txlist
# &address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a
# &startblock=0
# &endblock=99999999
# &page=1 Used in case w have more than 10K transactions
# &offset=10
# &sort=asc
# &apikey=YourApiKeyToken
def get_transactions(address):
    get_transactions_url = make_api_url(
        "account",
        "txlist",
        address,
        startblock=0,
        endblock=99999999,
        page=1,
        offset=10000,
        sort="asc",
    )  # Pass them as arguments as it's defined with KWARGS
    response = get(get_transactions_url)
    data = response.json()["result"]

    # We have/need almost the same data: only changes "txlist" for "txinternallist"
    internal_tx_url = make_api_url(
        "account",
        "txinternallist",
        address,
        startblock=0,
        endblock=99999999,
        page=1,
        offset=10000,
        sort="asc",
    )
    response2 = get(internal_tx_url)
    data2 = response2.json()["result"]

    data.extend(data2)  # Because it has
    data.sort(
        key=lambda x: int(x["timeStamp"])
    )  # For every element(represented by x), we're going to grab the time stamp

    # We will graph the Balance of the account (starting by 0) depending on its transactions
    # We could implement a user key to ask for account balance
    current_balance = 0
    balances = []
    times = []

    # Once we know the data that we want(we must display it first) we make variables to access it and being able to display it sorted
    for tx in data:
        to = tx["to"]
        from_address = tx["from"]
        value = int(tx["value"]) / ETHERVALUE

        if "gasPrice" in tx:
            gas = int(tx["gasUsed"]) * int(tx["gasPrice"]) / ETHERVALUE
        else:
            gas = int(tx["gasUsed"]) / ETHERVALUE

        time = datetime.fromtimestamp(
            int(float(tx["timeStamp"]))
        )  # To convert it to real time
        money_in = to.lower() == address.lower()  # to lower to make it more readable

        if money_in:
            current_balance += value
        else:
            current_balance -= value + gas
        # print("------------------")
        # print("To:", to)
        # print("From:", from_address)
        # print("Value:", value)
        # print("Gas Comission:", gas)
        # print("Time:", time)

        balances.append(current_balance)
        times.append(time)

    # Using MATPLOTLIB to plot the graphs (Data Science)
    plt.plot(times, balances)
    plt.show()


get_transactions(address)
