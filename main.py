from web3_listener.contract_listener import Web3ContractListener
from web3_listener.secret import get_secrets_from_string
import os


if __name__ == "__main__":
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-creds.json"

    #ETH_URL = get_secrets_from_string(os.environ["SECRET_INFURA"])
    ETH_URL = get_secrets_from_string("projects/148433842428/secrets/infura-listener/versions/1")

    ETH_URL = f"https://rinkeby.infura.io/v3/{ETH_URL}"
    # ETH_URL = f"https://mainnet.infura.io/v3/{ETH_URL}"

    #ETHERSCAN_TOKEN = get_secrets_from_string(os.environ["SECRET_ETHERSCAN"])
    ETHERSCAN_TOKEN = get_secrets_from_string("projects/148433842428/secrets/etherscan-listener/versions/1")

    contract_address = "0xFC5F3D1Cd0710702FB6D461b8718adB947c88388"

    contract_listener = Web3ContractListener(
        eth_url=ETH_URL,
        contract_address=contract_address,
        etherscan_token=ETHERSCAN_TOKEN,
    )
    contract_listener.listen()
