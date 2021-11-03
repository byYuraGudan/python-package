from package.functions import is_equal
import os

def test_equal():
    print(os.getenv("BES_SECRET"))
    assert is_equal(1, 1), "Is not correct value"


def test_valid():
    pass


def test_valid2():
    pass


def test_valid3():
    pass


def test_valid4():
    pass
