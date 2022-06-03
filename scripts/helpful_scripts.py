from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTVALUE = 200000000000
LOCAL_HOSTS_ADDRESS = ["development","ganache-local"]

def get_account():
    if network.show_active() in LOCAL_HOSTS_ADDRESS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"active network is: {network.show_active()}")
    print("Mock Contract is deploying")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTVALUE, "ether"), {"from": get_account()})
    print("Mock Contract Deployed!")
