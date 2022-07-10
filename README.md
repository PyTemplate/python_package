```bash

   ___        _____                         _         _
  / _ \ _   _/__   \ ___  _ __ ___   _ __  | |  __ _ | |_  ___  ___
 / /_)/| | | | / /\// _ \| '_ ` _ \ | '_ \ | | / _` || __|/ _ \/ __|
/ ___/ | |_| |/ /  |  __/| | | | | || |_) || || (_| || |_|  __/\__ \
\/      \__, |\/    \___||_| |_| |_|| .__/ |_| \__,_| \__|\___||___/
        |___/                       |_|

```
<!-- source - https://patorjk.com/software/taag/#p=display&h=1&f=Ogre&t=PyTemplates -->

[![test workflow](https://github.com/PyTemplate/python_package/actions/workflows/test-and-lint.yaml/badge.svg)](https://github.com/PyTemplate/python_package/actions?query=workflow%3A%22Test+and+Lint%22++)
[![documentation workflow](https://github.com/PyTemplate/python_package/actions/workflows/pages/pages-build-deployment/badge.svg)](https://pytemplate.github.io/python_package/)
[![release workflow](https://github.com/PyTemplate/python_package/actions/workflows/release.yaml/badge.svg)](https://github.com/PyTemplate/python_package/releases/latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/PyTemplate/python_package/main.svg)](https://results.pre-commit.ci/latest/github/PyTemplate/python_package/main)
[![codecov](https://codecov.io/gh/PyTemplate/python_package/branch/main/graph/badge.svg?token=HG1NQ8HRA4)](https://codecov.io/gh/PyTemplate/python_package)
[![PyPI version](https://badge.fury.io/py/pytemplates_pypackage.svg)](https://pypi.org/project/pytemplates-pypackage/)

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
