from ossaudiodev import control_labels
from brownie import Key,accounts,config,network,System
def get_account(i):
    if network.show_active() == "development":
        return accounts[i]
    else:
        if(i == 1):
            return accounts.add(config["wallets"]["from_key"])
        else:
            return accounts.add(config["wallets"]["from_key_2"])
def deploy_key(account_number):
    account = get_account(account_number)
    Key.deploy({"from":account})
def hash(text,account_number):
    account = get_account(account_number)
    control_instance = Key[-1]
    return control_instance.hash(text,{"from":account})
    
