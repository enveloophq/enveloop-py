import requests

from .message_response import MessageResponse
from .template_response import TemplateResponse

class Client:
    """Client class."""

    def __init__(self, api_key=None, api_host=None, ssl=None):
        """Initialize the client."""
        self._api_key = api_key
        self._endpoint = 'https://{}'.format(api_host) if ssl else 'http://{}'.format(api_host)

    def send_message(self, template=None, to=None, from_address=None, subject=None, template_variables={}):
        data = {
            'to': to,
            'from': from_address,
            'subject': subject,
            'template': template,
            'template_variables': template_variables
        }

        res = requests.post(
            '{}/messages'.format(self._endpoint),
            json=data,
            headers={'Authorization': 'token {}'.format(self._api_key)}
        )

        return MessageResponse(status=res.status_code, message=res.json())

    def template_info(self, template=None):
        res = requests.get(
            '{}/templates/{}'.format(self._endpoint, template),
            headers={'Authorization': 'token {}'.format(self._api_key)}
        )

        return TemplateResponse(status=res.status_code, template=res.json())