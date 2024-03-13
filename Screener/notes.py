# API restrictions/limitations

x = 5456

start = 0
end = 500
while end < x:
    print(start, end)
    start = end
    end += 500
start = end - 500
end = x
print(start, end)

ameritrade = "3PIBTZW5VRXOP9WUSC2VRSGZN4RSZTMV"


def view(size):  # To avoid having to remember the names of the columns in
    start = 0
    stop = size
    while stop < len(df_best):
        print(df_best[start:stop])
        start = stop
        stop += size  # iteration kind like before
    print(df_best[start:stop])


# We can display them in different ways from console:
df_best.sort_values("PE")
pd.set_option("display.max_rows", 200)
df_symbols = df_peg["symbol"].tolist()
new = df["Symbol"].isin(df_symbol)
companies = df[new]
