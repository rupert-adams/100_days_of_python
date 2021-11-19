# Higher or Lower game, given two things, the user must guess if the follower count is higher or lower
# data and art provided, everything else is the challenge
import random
from .art import logo, vs
from .data import data as d1

def get_two_data_blocks(data: list = d1):
    data_dict = random.sample(data, 2)
    return data_dict


def main():
    get_two_data_blocks()

main()