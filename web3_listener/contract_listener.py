from web3 import Web3
import asyncio
import dataclasses
from etherscan import Etherscan


@dataclasses.dataclass
class Web3ContractListener:
    eth_url: str
    contract_address: str
    etherscan_token: str

    def __post_init__(self):
        self.w3 = Web3(Web3.HTTPProvider(self.eth_url))
        if self.eth_url.startswith("https://rinkeby"):
            eth_client = Etherscan(self.etherscan_token, net="rinkby")
        else:
            eth_client = Etherscan(self.etherscan_token)
        self.abi = eth_client.get_contract_abi(address=self.contract_address)
        self.contract = self.w3.eth.contract(
            address=Web3.toChecksumAddress(self.contract_address), abi=self.abi
        )
        self.event_filter = self.contract.events.myEvent.createFilter(
            fromBlock="latest"
        )

    def handle_event(self, event):
        print(f"processing transaction {Web3.toJSON(event)}")
        # todo here we will send an async request to the backend to process the tx with the code doing the mint stuff.

    async def log_loop(self, event_filter, poll_interval):
        while True:
            for event in event_filter.get_new_entries():
                print(event)
                self.handle_event(event)
            await asyncio.sleep(poll_interval)

    def listen(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.log_loop(self.event_filter, 2))
