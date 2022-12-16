from .client import Client

def connect(api_key, api_host='api.enveloop.com', ssl=True):
    """Return an initialized instance of Client."""
    return Client(api_key, api_host, ssl)