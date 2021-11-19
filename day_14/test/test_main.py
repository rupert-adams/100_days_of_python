from src.main import get_two_data_blocks, compare
from operator import itemgetter


EXPECTED_TWO_DATA_BLOCKS = [
    {
        'name': 'Website A',
        'follower_count': 200,
        'description': 'The superior website',
        'country': 'Cuba'
    },
    {
        'name': 'Website B',
        'follower_count': 100,
        'description': 'The inferior website',
        'country': 'Portugal'
    }
]

EXPECTED_COMPARISON = 'Website A'

def test_get_two_data_blocks(data_block):
    f = itemgetter("name")
    item_1, item_2 = get_two_data_blocks(data_block)
    result = sorted([item_1, item_2], key=f)
    comparison = sorted(list(EXPECTED_TWO_DATA_BLOCKS), key=f)
    assert result == comparison

def test_compare(data_block):
    block_1, block_2 = get_two_data_blocks(data_block)
    comparison = EXPECTED_COMPARISON
    result = compare(block_1, block_2)
    assert result == comparison 
