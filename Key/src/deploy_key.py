from solcx import compile_standard
from web3 import Web3
from web3.middleware import geth_poa_middleware
import os
from dotenv import load_dotenv
import json
load_dotenv()
with open("../contracts/Key.sol","r") as file:
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
with open("../build/Key.json","w") as file:
    json.dump(compiled_sol,file)
bytecode = compiled_sol["contracts"]["Key.sol"]["Key"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["Key.sol"]["Key"]["abi"]
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/5d258151666444148f94223be0641c12"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
chain_id = 4
my_address = "0x3a76eBa708a88aEf87d3906dCEbAC90A4F9C974b"
private_key = os.getenv("PRIVATE_KEY_1")
Key = w3.eth.contract(abi=abi,bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)
tx = Key.constructor().buildTransaction(
    {"chainId":chain_id,"from":my_address,"nonce":nonce}
)
sx = w3.eth.account.sign_transaction(tx,private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(sx.rawTransaction)
tx_recept = w3.eth.wait_for_transaction_receipt(tx_hash)
with open("key_transaction.txt","w") as file:
    file.write(str(tx_recept.contractAddress))

