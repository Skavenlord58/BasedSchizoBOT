# Based Schizo
## A schizo impersonation bot

### Introduction
TODO

### Development

This package uses [uv](https://docs.astral.sh/uv/) and python 3.12.

Make sure you make `.env` file with proper env vars.

#### Develop Locally

Install dependencies:
```shell
uv sync --frozen
```

run the script locally:
```shell
uv run main.py
```

Lock dependencies:
```shell
uv lock
```

#### Checks and tests

Run formatting:
```shell
uv run ruff check --fix
```

Check the formatting
```shell
uv run ruff check
```

Run tests:
```shell
uv run pytest
```

#### Run in docker

Build and run the image:
```shell
docker compose up --build
```

### Lexical analysis notes

In order to make proper dad jokes or your mom jokes in czech, 
the bot uses [Morphodita](https://ufal.mff.cuni.cz/morphodita/api-reference#python_bindings)
with [python bindings](https://pypi.org/project/ufal.morphodita/) and models downloaded from [here](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-4794).

Models are downloaded using

```shell
curl --remote-name-all https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-4794/czech-morfflex2.0-pdtc1.0-220710.zip
```

you can try it online [here](https://lindat.mff.cuni.cz/services/morphodita/)

