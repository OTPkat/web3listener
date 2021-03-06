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

    def delete_mints(self):
        token = self.get_bearer_token()
        headers = {
            f"Authorization": f"Bearer {token}",
        }
        response = requests.post(
            f"{self.url}/clear_nfts/", headers=headers
        )
        return response

    def delete_passwords(self):
        token = self.get_bearer_token()
        headers = {
            f"Authorization": f"Bearer {token}",
        }
        response = requests.post(
            f"{self.url}/clear_passwords/", headers=headers
        )
        return response

    def create_passwords(self, amount: int):
        token = self.get_bearer_token()
        headers = {
            f"Authorization": f"Bearer {token}",
        }
        response = requests.post(
            f"{self.url}/create_passwords/", headers=headers, params={"amount": amount }
        )
        return response

    def get_passwords(self):
        token = self.get_bearer_token()
        headers = {
            f"Authorization": f"Bearer {token}",
        }
        response = requests.get(
            f"{self.url}/passwords_mint/", headers=headers
        )
        return response
