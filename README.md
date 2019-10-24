## Awesome Poll app

[![Build Status](https://travis-ci.org/wandersonsc/awesome-poll.svg?branch=master)](https://travis-ci.org/wandersonsc/awesome-poll) [![codecov](https://codecov.io/gh/wandersonsc/awesome-poll/branch/master/graph/badge.svg)](https://codecov.io/gh/wandersonsc/awesome-poll)

### Poll site using best practices for Test Driven Development (TDD) & Pytest

## Technology Stack

- Python
- Travis
- Pytest

## Get the code and start the server.

1. Get the code:

```
git clone https://github.com/wandersonsc/awesome-poll
```

2. Run it! Assuming you have Python setup, run the following commands:

```sh
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver

```

## Testing

To run the tests, check your test coverage, and generate a simplified coverage report & flake8:

```sh
pytest or pytest & flake8

```
