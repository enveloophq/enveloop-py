# Enveloop

enveloop-py is a python wrapper for the Enveloop API. It allows easy use of the API to send messages.

## Installation

Install with pip:

```shell
python3 -m pip install enveloop-py
```

## Usage

Setup the client connection:

```python
import os
from enveloop_py import api

enveloop = api.connect(os.environ['ENVELOOP_API_TOKEN'])
```

Send a message: 

```python
enveloop.send_message(
  template='welcome-email',
  to='user@email.com',
  from_address='welcome@myapp.com',
  subject='Welcome to MyApp',
  template_variables={
    "first_name": 'John',
  }
)
```

Get information about a template (variables and body html):

```python
enveloop.template_info(template='welcome-email')
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/enveloophq/enveloop-ruby. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [code of conduct](https://github.com/enveloophq/enveloop-ruby/blob/master/CODE_OF_CONDUCT.md).


## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the Enveloop project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/enveloophq/enveloop-ruby/blob/master/CODE_OF_CONDUCT.md).
