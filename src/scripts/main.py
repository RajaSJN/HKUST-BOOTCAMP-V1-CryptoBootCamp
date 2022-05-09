# from brownie import System,accounts,config,network
# from scripts.utils_key import *
# from scripts.utils_system import *
from ossaudiodev import control_labels
# from brownie import accounts,config,network
import brownie as br
def get_account(i):
    if br.network.show_active() == "development":
        return br.accounts[i]
    else:
        print(type(br.config))
        if(i == 1):
            return br.accounts.add("51fb99fe179b38a4aefb9b8e25be309a9046543a18f2b4c79b343502aa229267")
        else:
            return br.accounts.add(br.config["wallets"]["from_key_2"])
def deploy_key(account_number):
    account = get_account(account_number)
    br.Key.deploy({"from":account})
def hash(text,account_number):
    account = get_account(account_number)
    control_instance = br.Key[-1]
    return control_instance.hash(text,{"from":account})
def main():
    deploy_key(1)
    hash("Patrick",1)
    # contract_instance = System[-1]
    # account = get_account(1)
    # account2 = get_account(2)
    # print(contract_instance.getKey({"from":account}))
    # contract_instance.addUser(account2,{"from":account})
    # contract_instance.grantSudo(account2,{"from":account})
    # print(contract_instance.getKey({"from":account2}))
    #print(contract_instance.getKey({"from":account2}))