from python_package.core.module1 import greet


def test_greet():
    hello = greet(user="Jacob")
    assert hello == "Hello Jacob!"
