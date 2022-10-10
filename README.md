# Refactored Enigma Backend

Refactored Enigma (code name) is a project to create an efficient and easy to use notes' application. This repository contains the backend code for [refactored enigma project](https://github.com/AlexisDominguez/refactored-enigma).

# Installation

## Pre-requisites

- Python 3.7.0
- Postgresql

## Installation Process

To start using this project, we recommend you to first create a virtual environment for your python dependencies to avoid dependencies conflicts.

Install python's virualenv dependency:

```
pip3 install virtualenv
```

Create a new virtual environment:

```
virtualenv -p python3 .venv
```

Activate your virtual environmnet:

```
# MacOs
source .venv/bin/activate

# Windows
.venv\Scripts\activate.bat
```

Install project dependencies:

```
pip install -r requirements.txt
```

Run migrations for your database:

```
python manage.py migrate
```

Run django's server:

```
python manage.py runserver
```

And we are done! Now we can start messing around with the project's functionality!
