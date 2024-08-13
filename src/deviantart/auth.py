import httpx_auth
from lapidary.runtime import NamedAuth


def client_creds(client_id: str, client_secret: str) -> NamedAuth:
    return 'open', httpx_auth.OAuth2ClientCredentials(
        'https://www.deviantart.com/oauth2/token',
        client_id,
        client_secret
    )
