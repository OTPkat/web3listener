import requests
import google.auth.transport.requests
import google.oauth2.id_token
import dataclasses

from pydantic import BaseModel
from typing import Optional
import json


class ArchiveMint(BaseModel):
    token_id: int
    method: str
    hash: Optional[str]


@dataclasses.dataclass
class MintPoster:
    url: str = "https://archive-mint-backend-s7ftrbvx6q-ez.a.run.app"

    def get_bearer_token(self):
        auth_req = google.auth.transport.requests.Request()
        token = google.oauth2.id_token.fetch_id_token(auth_req, self.url)
        return token

    def send_archive_mint(self, archive_mint: ArchiveMint):
        token = self.get_bearer_token()
        headers = {
            f"Authorization": f"Bearer {token}",
        }
        response = requests.post(
            f"{self.url}/archive_mint/", headers=headers, data=json.dumps(archive_mint.dict()).encode('utf-8')
        )
        return response

    def get_mints(self):
        token = self.get_bearer_token()
        headers = {
            f"Authorization": f"Bearer {token}",
        }
        response = requests.get(
            f"{self.url}/archive_nfts/", headers=headers
        )
        return response


if __name__ == '__main__':
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../gcp-creds.json"
    # print(MintPoster().send_archive_mint(ArchiveMint(**{
    #     "hash": "0xTopkkekw",
    #     "method": "publicMint",
    #     "token_id": 12
    # })))
    # print(MintPoster().get_mints().json())
