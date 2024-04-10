class Message:
    """Message class."""

    def __init__(self, api_response={}):
        """Initialize the template."""
        self._message_id = api_response['messageId']
        self._to = api_response['to']
        self._from_address = api_response['from']
        self._body = api_response['body']

    @property
    def message_id(self):
        """Return the subject."""
        return self._message_id

    @property
    def to(self):
        """Return the subject."""
        return self._to

    @property
    def from_address(self):
        """Return the subject."""
        return self._from_address

    @property
    def body(self):
        """Return the body."""
        return self._body
