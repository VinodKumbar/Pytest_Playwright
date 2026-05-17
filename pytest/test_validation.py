
import pytest


@pytest.fixture(scope="module")
def pre_setup():
    print("Module Scope : I set up Browser Instance")
    return "pass"

@pytest.fixture(scope="function")
def post_setup():
    print("Function Scope : Post pre-set up")
    yield
    print("Tear Down Validation")
@pytest.mark.smoke
def test_initial_check(pre_setup, post_setup):
    print("This is first test")
    assert pre_setup == "pass"

@pytest.mark.skip
def test_second_check(pre_setup, post_setup):
    print("This is second test")
