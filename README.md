<p align="center">
  <a href="https://user-images.githubusercontent.com/20674972/178172752-abd4497d-6a0e-416b-9eef-1b1c0dca8477.png">
    <img src="https://user-images.githubusercontent.com/20674972/178172752-abd4497d-6a0e-416b-9eef-1b1c0dca8477.png" alt="Pytemplates Banner" style="width:100%;">
  </a>
</p>

<p align="center">
  <a href="https://github.com/PyTemplate/python_package/actions/workflows/test.yaml">
    <img src="https://github.com/PyTemplate/python_package/actions/workflows/test.yaml/badge.svg" alt="Test status">
  </a>

  <a href="https://github.com/PyTemplate/python_package/actions/workflows/lint.yaml">
    <img src="https://github.com/PyTemplate/python_package/actions/workflows/lint.yaml/badge.svg" alt="Linting status">
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

## Commands

`make clean`                clean all build, testing, and static documentation files
`make lint`                 run autoformaters and linters
`make test`                 run tests
`make check`                run linters and tests, then cleanup
`make gen-docs`             generate Sphinx HTML documentation
`make docs`                 generate Sphinx HTML documentation and serve to browser
`make pre-release`          bump the version and create the release tag
`make release`              push the release tag and trigger the release pipeline

## Workflows

`lint`                      run autoformaters and linters on every push/pull_request to the *main* branch
`test`                      run tests on every push/pull_request to the *main* branch
`build-and-release`         release the package on PyPI upon tag creation
