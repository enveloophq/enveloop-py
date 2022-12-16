class TemplateResponse:
    """TemplateResponse class."""

    def __init__(self, status=None, template=None):
        """Initialize the response."""
        self._status = status
        self._template = template

    @property
    def status(self):
        """Return the status."""
        return self._status

    @property
    def template(self):
        """Return the template."""
        return self._template