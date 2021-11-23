from src.main import report, check_levels, coin_process

EXPECTED_REPORT = "Report:\nwater: 300ml\nmilk: 200ml\ncoffee: 100mg"
EXPECTED_FAILURE = False
EXPECTED_SUCCESS = True

def test_report(machine_data_block):
    result = report(machine_data_block["machine"])
    assert result == EXPECTED_REPORT

def test_check_levels_failed(coffee_data_block, machine_data_block):
    coffee = "extreme_test_coffee"
    result = check_levels(coffee, machine_data_block["machine"], coffee_data_block)
    assert result == EXPECTED_FAILURE

def test_check_levels_succeeded(coffee_data_block, machine_data_block):
    coffee = "cheap_test_coffee"
    result = check_levels(coffee, machine_data_block["machine"], coffee_data_block)
    assert result == EXPECTED_SUCCESS

def test_coin_process_too_little(coffee_data_block, machine_data_block):
    test_coin_list = [1, 0.50]
    result = coin_process(test_coin_list, coffee_data_block["extreme_test_coffee"]["price"], machine_data_block["accepted coins"])
    assert result == EXPECTED_FAILURE

def test_coin_process_wrong_coin(coffee_data_block, machine_data_block):
    test_coin_list = [1, 0.50, 0.25]
    result = coin_process(test_coin_list, coffee_data_block["extreme_test_coffee"]["price"], machine_data_block["accepted coins"])
    assert result == EXPECTED_FAILURE

def test_coin_process_just_right(coffee_data_block, machine_data_block):
    test_coin_list = [0.50, 0.50]
    result = coin_process(test_coin_list, coffee_data_block["cheap_test_coffee"]["price"], machine_data_block["accepted coins"])
    assert result == EXPECTED_SUCCESS