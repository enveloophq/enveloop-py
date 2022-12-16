class MessageResponse:
    """MessageResponse class."""

    def __init__(self, status=None, message=None):
        """Initialize the response."""
        self._status = status
        self._message = message

    @property
    def status(self):
        """Return the status."""
        return self._status

    @property
    def message(self):
        """Return the message."""
        return self._message