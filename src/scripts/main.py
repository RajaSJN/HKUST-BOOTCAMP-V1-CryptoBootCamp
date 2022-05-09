from brownie import Key,accounts,config,network,System
from scripts.utils_key import *
from scripts.utils_system import *
def main():
    deploy_key(1)
    #print(hash("patrick",1))
    # contract_instance = System[-1]
    # account = get_account(1)
    # account2 = get_account(2)
    # print(contract_instance.getKey({"from":account}))
    # contract_instance.addUser(account2,{"from":account})
    # contract_instance.grantSudo(account2,{"from":account})
    # print(contract_instance.getKey({"from":account2}))
    
