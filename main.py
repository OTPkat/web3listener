from web3_listener.contract_listener import Web3ContractListener
if __name__ == "__main__":
    import os
    ETHERSCAN_TOKEN = os.getenv("ETHERSCAN_TOKEN")
    ETH_URL = os.getenv("ETH_URL")
    contract_address = "0x39b2d948b13fa10054e00b9d5f5eea75d272fb32"
    contract_listener = Web3ContractListener(
        eth_url=ETH_URL,
        contract_address=contract_address,
        etherscan_token=ETHERSCAN_TOKEN,
    )
    contract_listener.listen()
