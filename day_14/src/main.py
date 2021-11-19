# Higher or Lower game, given two things, the user must guess if the follower count is higher or lower
# data and art provided, everything else is the challenge
import random
from .art import logo, vs
from .data import data as d1

def get_two_data_blocks(data: list = d1):
    '''
    Grabs 2 items from a given data list of dicts,
    defaults to list in data.py.
    '''
    data_blocks = random.sample(data, 2)
    item_1, item_2 = [data_blocks[i] for i in (0, 1)]
    return item_1, item_2

def compare(item_1: dict, item_2: dict):
    '''
    Given two correctly formatted dicts,
    the follower count will be compared and the name of the highest number will be returned.
    '''
    if item_1["follower_count"] > item_2["follower_count"]:
        return item_1["name"]
    elif item_2["follower_count"] > item_1["follower_count"]:
        return item_2["name"]



def game(data: list):
    '''
    game() runs compare() between two items chosen by get_two_data_blocks(),
    returns True if answer is correct, otherwise False
    '''
    item_1, item_2 = get_two_data_blocks(data)
    print(item_1["name"])
    print(vs)
    print(item_2["name"])
    answer = str(input("\nWhich has more followers?\n"))
    comparison = compare(item_1, item_2)
    if answer == comparison:
        print(f"Well done! {comparison} has more followers!")
        print("----------------------------\n\n")
        return True
    else:
        print("\nOops! You got it wrong I'm afraid! Game Over")
        print("----------------------------\n\n")
        return False

def main():
    '''
    While game_live is True, game() is run.
    If the answer is incorrect the game_live variable turns False, 
    displaying the score and ending the game.
    '''
    print(logo)
    print("----------------------------\n\n")
    print("Welcome to the Higher/Lower game!\n\nRules are simple: guess which of the two has a higher follower count,")
    print("if you are correct you score a point, if you are incorrect the game is over.\n")
    print("Lets Begin!\n\n")
    score = 0
    game_live = True
    while game_live:
        game_live = game(d1)
        score+=1
        if game_live == False:
            score-=1
            if score == 1:
                print(f"You scored {score} point!\n")
                break
            print(f"You scored {score} points!\n")
            break

if __name__ == "__main__":
    main()