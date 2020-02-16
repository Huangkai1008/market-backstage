# Market-Backstage

market-backstage is a Market backstage management system with [flask](https://flask.palletsprojects.com/).

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Contents

- [Quick Start](#Quick Start)
- [Usage](#Usage)
- [License](#License)

## Quick Start
1. Get the project
```bash
go -get https://github.com/Huangkai1008/market-backstage
```

2. Make sure you have installed [poetry](https://github.com/sdispater/poetry)
```bash
pip install poetry
poetry install                  # Add the libs
poetry shell                    # Start the virtualenv
```

3. Set environment variables
```bash
cp .env.example .env
```

3. Run it
```bash
flask run
```
## Usage

### Deployment
#### With Gunicorn
```bash
gunicorn autoapp:app
        --bind 127.0.0.1:5000
        -w 8
        -k eventlet
        --access-logfile -
        --error-logfile -
```


## License
[MIT](https://www.mit-license.org/)
