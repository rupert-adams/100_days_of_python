from src.main import report

EXPECTED_REPORT = "Report:\nwater: 300ml\nmilk: 200ml\ncoffee: 100mg"

def test_report(machine_data_block):
    assert report(machine_data_block["machine"]) == EXPECTED_REPORT