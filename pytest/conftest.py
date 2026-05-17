import pytest

@pytest.fixture(scope="session")
def pre_setup():
    print("Session Scope : I set up Browser Instance")