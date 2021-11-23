from src.main import report, check_levels

EXPECTED_REPORT = "Report:\nwater: 300ml\nmilk: 200ml\ncoffee: 100mg"
EXPECTED_LEVELS_FAILED = False
EXPECTED_LEVELS_SUCCEEDED = True

def test_report(machine_data_block):
    result = report(machine_data_block["machine"])
    assert result == EXPECTED_REPORT

def test_check_levels_failed(coffee_data_block, machine_data_block):
    coffee = "extreme_test_coffee"
    result = check_levels(coffee, machine_data_block["machine"], coffee_data_block)
    assert result == EXPECTED_LEVELS_FAILED

def test_check_levels_succeeded(coffee_data_block, machine_data_block):
    coffee = "cheap_test_coffee"
    result = check_levels(coffee, machine_data_block["machine"], coffee_data_block)
    assert result == EXPECTED_LEVELS_SUCCEEDED