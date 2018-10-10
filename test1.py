import pytest

@pytest.fixture()
def setUp():
    print("Am begining")

def test_A(setUp):
    print("method A")

def test_B(setUp):
    print("method B")