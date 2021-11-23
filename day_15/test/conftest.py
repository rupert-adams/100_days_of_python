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

@pytest.fixture
def machine_data_block():
    return test_machine_data
