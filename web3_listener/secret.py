import typing
from google.cloud import secretmanager


def get_secrets_from_string(secret_resource_id: str) -> str:
    """
    Assumes that the secret is stored as a dictionary
    """
    client_ = secretmanager.SecretManagerServiceClient()
    response = client_.access_secret_version(name=secret_resource_id)
    secret = response.payload.data.decode("UTF-8")
    return secret