class Template:
    """Template class."""

    def __init__(self, api_response={}):
        """Initialize the template."""
        self._template_variables = api_response['templateVariables']
        self._body = api_response['body']

    @property
    def template_variables(self):
        """Return the subject."""
        return self._template_variables

    @property
    def body(self):
        """Return the body."""
        return self._body
