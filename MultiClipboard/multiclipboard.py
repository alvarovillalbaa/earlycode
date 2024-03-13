import imp
from multiprocessing.spawn import import_main_path
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"
# data = clipboard.paste()
# print(data)

# json acts as library


def save_data(filepath, data):
    with open(filepath, "w") as f:
        # w makes the file be overwritten if already exists
        json.dump(data, f)


# save_items("test.json", {"key": "value"})


def load_data(filepath):
    try:  # we use try and except for when we're not certain if it'll give an error
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


# What we're committing input, we should always create a file with the information(in this case a json with dictionaries)
# for the program to run commands(commands personalisation)
if len(sys.argv) == 2:  # There counts the implicit file plus the command we want
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key:")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Key does not exist")
        print("Data loaded!")
    elif command == "list":
        print(data)

    else:
        print("Unknown command.")
else:
    print("Only one command is allowed.")
