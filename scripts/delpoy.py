from distutils.command.config import config
from brownie import FundMe, network, MockV3Aggregator, config
from scripts.helpful_scripts import deploy_mocks, get_account, LOCAL_HOSTS_ADDRESS


def depoy_fund_me():
    account = get_account()

    # pass rinkeby address or mock address? depends on which network is used
    if network.show_active() not in LOCAL_HOSTS_ADDRESS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    # pass priceFeed address as first parameter to our contract constructor method
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"fund me contract deployed on this address: {fund_me.address}")
    return fund_me


def main():
    depoy_fund_me()
