from ossaudiodev import control_labels
from brownie import Key,accounts,config,network
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
def deploy():
    account = get_account()
    Key.deploy({"from":account})
def hash(text):
    account = get_account()
    control_instance = Key[-1]
    return control_instance.hash(text,{"from":account})
    
