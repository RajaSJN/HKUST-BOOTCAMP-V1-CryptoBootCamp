from dis import Bytecode
from solcx import compile_standard
import json
with open("./contracts/Key.sol","r") as file:
    key_file = file.read()
compiled_sol = compile_standard(
    {
    "language":"Solidity",
    "sources":{"Key.sol":{"content":key_file}},
    "settings":{
        "outputSelection": {
            "*":{
                "*": ["abi","metadata","evm.bytecode","evm.bytecode.sourceMap"]
            }
        }
    }
    },
    solc_version="0.8.13",
)
with open("./bin/Key.json","w") as file:
    json.dump(compiled_sol,file)
bytecode = compiled_sol["contracts"]["Key.sol"]["Key"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["Key.sol"]["Key"]["abi"]
