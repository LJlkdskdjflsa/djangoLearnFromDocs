import pytest


@pytest.fixture(scope="session")
def fixture_1():
    print("fixture 1")
    return 1


def test_example_1(fixture_1):
    num1 = fixture_1
    assert num1 == 1

def test_example_2(fixture_1):
    print("fixture 2")

    num1 = fixture_1
    assert num1 == 1