<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Description](#description)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)

<!-- ABOUT THE PROJECT -->

## Description

`test-project-sma` is a Python service that imitates [SMA](https://www.investopedia.com/terms/s/sma.asp) calculation based on close price values received from [Ticker](https://binance-docs.github.io/apidocs/spot/en/#individual-symbol-mini-ticker-stream). It exposes SMA for 7, 25 or 99 periods, ticker update speed (1000 ms) is used as a period.

### Technologies

This microservice is written with Python 3.9.

Dependencies:

- [fastapi](https://fastapi.tiangolo.com/) - high-performance web-framework
- [uvicorn](https://github.com/encode/uvicorn) - lightning-fast ASGI server
- [websockets](https://github.com/aaugustin/websockets) - robust library to implement websocket client/server

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

To run this locally you'll need [Python 3.9](https://www.python.org/downloads/). You may use [pipenv](https://pipenv.pypa.io/en/latest/) to maintain virtual environment and dependencies.

### Installation

1. Clone the repo

```sh
git clone https://github.com/pgodlevska/test-project-sma.git
```

2. If you use pipenv, then run in your shell:

```sh
$ cd test-project-sma
$ pipenv shell
$ pipenv install
```

If you don't have pipenv installed, then:

```sh
$ cd test-project-sma
$ python -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

### Usage

To run application:

Activate virtual environment.

- Then run:

```sh
$ uvicorn app.main:app --reload
```

- Or set up `PYTHONPATH` (if needed) and run app via python:

```sh
$ export PYTHONPATH=$PYTHONPATH:$(pwd)
$ python app/main.py
```

Check if service started at root endpoint `127.0.0.1:8000/`

Check service API docs at `127.0.0.1:8000/docs`
