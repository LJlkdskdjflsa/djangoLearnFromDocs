import pytest


@pytest.fixture(scope="session")
def yield_fixture():
    print("Start test phase")
    yield 6
    print("End test phase")


def test_example_2(yield_fixture):
    print("fixture 2")

    assert yield_fixture == 6