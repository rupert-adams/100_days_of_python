import pytest

test_data = [
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

num_1, num_2 = 1,2

@pytest.fixture
def data_block():
    return test_data
