# !!!! Brain Hacked !!!!! Lets Go

## Step 1 - Create Virtual Environment and activate

Setup your virtual env

Ubuntu or macOS

```sh
python3 -m  venv venv
source venv/bin/activate
```

Windows

```cmd
python -m venv venv
.\venv\Scripts\activate
```

## Step 2 - Install Poetry and dependencies

Install Poetry: https://python-poetry.org/

```sh
pip install poetry
poetry install
```

## Step 3 - Connect with database

Lets connect With database (Read more: https://tortoise.github.io/toc.html)

```bin
aerich init -t base.settings.TORTOISE_ORM
```

this creates migration folder

## Step 4 - Inspect build on session table
