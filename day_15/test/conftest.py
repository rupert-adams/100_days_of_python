import pytest

test_machine_data = {
    "machine": {
      "water": 300,
      "milk": 200,
      "coffee": 100
    },
    "accepted coins": [
      1,
      2,
      0.5,
      0.1,
      0.05,
      0.02,
      0.01
    ]
  }

test_coffee_data = {
  "cheap_test_coffee": {
    "water": 25,
    "coffee": 2,
    "milk": 10,
    "price": 1
  },
  "extreme_test_coffee": {
    "water": 2500,
    "coffee": 240,
    "milk": 1000,
    "price": 30
  }
}

@pytest.fixture
def machine_data_block():
    return test_machine_data

@pytest.fixture
def coffee_data_block():
    return test_coffee_data
