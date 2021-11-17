# Number guessing game with two settings, easy and hard.
# Easy is 10 tries, hard is 5
# Must guess a number between 1 and 100 and the computer will tell you if it is higher or lower

import random
from art import logo

def difficulty_select():
    DIFFICULTY_TURNS = {
        'Easy': 10,
        'Hard': 5
    }
    difficulty = str(input("choose a difficulty, 'Easy' or 'Hard':")).capitalize()
    while difficulty not in list(DIFFICULTY_TURNS.keys()):
        difficulty = str(input("Input not recognized, Please choose 'Easy' or 'Hard':")).capitalize()
    print(f"You have selected {difficulty}, you have {DIFFICULTY_TURNS[difficulty]} turns!")
    return DIFFICULTY_TURNS[difficulty]

def guess(turns, comp_num):
    print("Guess the number between 1 and 100")
    guess = int(input("Please guess the number:"))
    while turns > 0:
        if (guess > 100 or guess < 1):
            print(f'---\nIt was a simple task, choose a number between 1 and 100.\nThe game is over')
            break
        if guess > comp_num:
            turns-=1
            guess = int(input(f"too high, {turns} turns remain. Guess again:\n"))
            print("----")
        elif guess < comp_num:
            turns-=1
            guess = int(input(f"too low, {turns} turns remain. guess again:\n"))
            print("----")
        else:
            turns=0
            print(f"Number was {comp_num}, Congratulations, you win!")

def guessing_game():
    comp_num = random.randint(1,100)
    print(logo)
    print("Welcome to the number guessing game!")
    try:
        turns = difficulty_select()
        guess(turns, comp_num)
    except:
        print('---\nThe guess needs to be a number,\nYou have failed to grasp even the simplest of concepts,\nThe game is over')

if __name__ == "__main__":
    guessing_game()
