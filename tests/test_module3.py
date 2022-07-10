from pytemplates_pypackage.core.module3 import delete


def test_delete():
    goodbye = delete(user="Jacob")
    assert goodbye == "Delete Jacob!"
