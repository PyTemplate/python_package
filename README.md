```bash

   ___        _____                         _         _
  / _ \ _   _/__   \ ___  _ __ ___   _ __  | |  __ _ | |_  ___  ___
 / /_)/| | | | / /\// _ \| '_ ` _ \ | '_ \ | | / _` || __|/ _ \/ __|
/ ___/ | |_| |/ /  |  __/| | | | | || |_) || || (_| || |_|  __/\__ \
\/      \__, |\/    \___||_| |_| |_|| .__/ |_| \__,_| \__|\___||___/
        |___/                       |_|

```
<!-- source - https://patorjk.com/software/taag/#p=display&h=1&f=Ogre&t=PyTemplates -->

<p align="center">
  <a href="https://github.com/PyTemplate/python_package/actions?query=workflow%3A%22Test+and+Lint%22++">
    <img src="https://github.com/PyTemplate/python_package/actions/workflows/test-and-lint.yaml/badge.svg" alt="Test and lint status">
  </a>
  
  <a href="https://results.pre-commit.ci/latest/github/PyTemplate/python_package/main">
    <img src="https://results.pre-commit.ci/badge/github/PyTemplate/python_package/main.svg" alt="pre-commit.ci status">
  </a>
  
  <a href="https://codecov.io/gh/PyTemplate/python_package">
    <img src="https://codecov.io/gh/PyTemplate/python_package/branch/main/graph/badge.svg?token=HG1NQ8HRA4" alt="Code coverage status">
  </a>
  
  <a href="https://pypi.org/project/pytemplates-pypackage/">
    <img src="https://badge.fury.io/py/pytemplates_pypackage.svg" alt="PyPI version">
  </a>
</p>

## Description

A basic python package template which includes proper package structure with a functioning package installation. The package is built using poetry; metadata and dependency information is stored in the pyproject.toml. This template includes flake8, pylint, isort, and pytest settings with configurations compatible with the black autoformatter. Pylint settings are based on the Google style standards for python and adapted for black compatibility.  Testing is automated using github workflows, codecov.io, and pre-commit.ci. Application deployment is managed using multi-staged docker builds for fast develop/deploy cycles.

## Setup

Using `poetry`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
poetry install --no-dev
```

## Usage

From a `.py` file:

```python
import pytemplates
pytemplates.__version__
pytemplates.greet(user="Jacob")

from pytemplates import wish_farewell
wish_farewell(user="Jacob")
```

## Development Setup

Using `poetry`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
poetry install
```

## Testing

To run the tests locally using the development environment:

```bash
cd pytemplates
poetry run pytest
```

## Documentation

To build and view the documentation locally using the development environment:

```bash
cd pytemplates/docs
make html
google-chrome build/html/index.html
```
