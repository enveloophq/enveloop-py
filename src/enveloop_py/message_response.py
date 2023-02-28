from .message import Message

class MessageResponse:
    """MessageResponse class."""

    def __init__(self, response=None):
        if response is None:
            return

        self._status = response.status_code
        body = response.json()

        if self._status == 200:
            self._message = Message(body)
            self._error = None
        else:
            raise RuntimeError(body['error'])

    @property
    def status(self):
        """Return the status."""
        return self._status

    @property
    def message(self):
        """Return the message."""
        return self._message

    @property
    def error(self):
        """Return the error."""
        return self._error
