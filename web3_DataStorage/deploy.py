from solcx import compile_standard

with open("./DataStorage.sol", "r") as file:
    data_storage_file = file.read()
    print(data_storage_file)

# Compile Our Solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"DataStorage.sol": {"content": data_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]},
                }
            }
        },
    },
)

with open("./DataStorage.sol", "r") as file:
    json.dumop(compiled_sol, file)

print(compiled_sol)

# get bytecode
bytecode = compiled_sol["contracts"]["DataStorage.sol"]["DataStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["DataStorage.sol"]["DataStorage"]["abi"]
