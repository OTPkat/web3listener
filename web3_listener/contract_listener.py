from web3 import Web3
import asyncio
import dataclasses
from etherscan import Etherscan
from web3_listener.mint_poster import ArchiveMint, MintPoster
import pdb


@dataclasses.dataclass
class Web3ContractListener:
    eth_url: str
    contract_address: str
    etherscan_token: str

    def __post_init__(self):
        self.w3 = Web3(Web3.HTTPProvider(self.eth_url))
        if self.eth_url.startswith("https://rinkeby"):
            eth_client = Etherscan(self.etherscan_token, net="rinkeby")
        else:
            eth_client = Etherscan(self.etherscan_token)
        self.abi = eth_client.get_contract_abi(address=self.contract_address)
        self.contract = self.w3.eth.contract(
            address=Web3.toChecksumAddress(self.contract_address), abi=self.abi
        )
        self.event_filter = self.contract.events.mint.createFilter(
            fromBlock="latest",
        )

    @staticmethod
    def send_mint_event(event):
        event_mint = {
            "token_id": event.args._tokenId,
            "method": event.args._method,
            "hash": event.args._hash
        }
        archive_mint = ArchiveMint(**event_mint)
        MintPoster().send_archive_mint(archive_mint=archive_mint)

    async def log_loop(self, event_filter, poll_interval):
        while True:
            for event in event_filter.get_new_entries():
                print(event)
                self.send_mint_event(event)
            await asyncio.sleep(poll_interval)

    def listen(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.log_loop(self.event_filter, 12))
