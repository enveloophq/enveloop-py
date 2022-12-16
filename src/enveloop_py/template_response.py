from .template import Template

class TemplateResponse:
    """TemplateResponse class."""

    def __init__(self, response=None):
        if response is None:
            return

        self._status = response.status_code
        body = response.json()

        if self._status == 200:
            self._template = Template(body)
            self._error = None
        elif self._status == 500:
            self._template = None
            self._error = body['error']
        else:
            self._template = None
            self._error = 'Unknown error'

    @property
    def status(self):
        """Return the status."""
        return self._status

    @property
    def template(self):
        """Return the template."""
        return self._template

    @property
    def error(self):
        """Return the error."""
        return self._error
