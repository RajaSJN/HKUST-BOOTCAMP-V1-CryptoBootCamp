from web3 import Web3
from web3.middleware import geth_poa_middleware
import os
from dotenv import load_dotenv
import json
import codecs
load_dotenv()
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/5d258151666444148f94223be0641c12"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
f = open('./build/Key.json')
data = json.load(f)
f.close()
abi = data["contracts"]["Key.sol"]["Key"]["abi"]
with open("key_transaction.txt","r") as file:
    address = file.readline()
contract_instance = w3.eth.contract(address=address,abi=abi)
def rand():
    return contract_instance.functions.rand().call()
def hash(string):
    return contract_instance.functions.hash(string).call()




