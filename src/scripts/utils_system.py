from audioop import add
from brownie import accounts,config,network,System
def get_account(i):
    if network.show_active() == "development":
        return accounts[i]
    else:
        if(i == 1):
            return accounts.add(config["wallets"]["from_key"])
        else:
            return accounts.add(config["wallets"]["from_key_2"])
def deploy_system(verification,account_number):
    account = get_account(account_number)
    System.deploy(verification,{"from":account})
def getKey():
    contract_instance = System[-1]
    return contract_instance.getKey()
def addUser(address,account_number):
    contract_instance = System[-1]
    account = get_account(account_number)
    tx = contract_instance.addUser(address,{"from":account})
    tx.wait(1)
def removeUser(address,account_number):
    contract_instance = System[-1]
    account = get_account(account_number)
    tx = contract_instance.removeUser(address,{"from":account})
    tx.wait(1)
def grantSudo(address,account_number):
    contract_instance = System[-1]
    account = get_account(account_number)
    tx = contract_instance.grantSudo(address,{"from":account})
    tx.wait(1)