from ossaudiodev import control_labels
# from brownie import accounts,config,network
import brownie as br
def get_account(i):
    if br.network.show_active() == "development":
        return br.accounts[i]
    else:
        print(type(br.config))
        if(i == 1):
            return br.accounts.add(br.config["wallets"]["from_key"])
        else:
            return br.accounts.add(br.config["wallets"]["from_key_2"])
def deploy_key(account_number):
    account = get_account(account_number)
    br.Key.deploy({"from":account})
def hash(text,account_number):
    account = get_account(account_number)
    control_instance = br.Key[-1]
    return control_instance.hash(text,{"from":account})

