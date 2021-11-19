from src.main import get_two_data_blocks
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

def test_get_two_data_blocks(data_block):
    f = itemgetter("name")
    result = sorted(list(get_two_data_blocks(data_block)),key=f)
    comparison = sorted(list(EXPECTED_TWO_DATA_BLOCKS), key=f)
    assert result == comparison

