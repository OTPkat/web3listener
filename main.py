from web3_listener.contract_listener import Web3ContractListener
from web3_listener.secret import get_secrets_from_string


if __name__ == "__main__":
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-creds.json"

    ETH_URL = get_secrets_from_string("projects/148433842428/secrets/infura-listener/versions/1")
    ETHERSCAN_TOKEN = get_secrets_from_string("projects/148433842428/secrets/etherscan-listener/versions/1")

    ETH_URL = f"https://rinkeby.infura.io/v3/{ETH_URL}"
    # ETH_URL = f"https://mainnet.infura.io/v3/{ETH_URL}"

    contract_address = "0x7eC1C71461Fd1BA75B00864e3fc2cDAda12e48a8"

    contract_listener = Web3ContractListener(
        eth_url=ETH_URL,
        contract_address=contract_address,
        etherscan_token=ETHERSCAN_TOKEN,
    )
    contract_listener.listen()
