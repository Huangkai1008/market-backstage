# Market-Backstage

market-backstage is a Market backstage management system with [flask](https://flask.palletsprojects.com/).

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Contents

- [QuickStart](#QuickStart)
- [Usage](#Usage)
- [License](#License)

## QuickStart
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

4. Run it
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

#### With Docker
1.Build image
```bash
docker build -t market-backstage:0.1.0 .
```

2.Start service with docker-compose
```bash
docker create network market-backstage

docker-compose up -d
```

## License
[MIT](https://www.mit-license.org/)
