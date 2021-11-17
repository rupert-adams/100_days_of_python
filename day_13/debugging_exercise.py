############DEBUGGING#####################

# # Describe Problem
def my_function():
    # range was between 1,20. Changed to 1,21
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# randint was between 1,6. Changed to 0,5 to fit the indexes.
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth?"))
# Added '=' to each side of the statement to account for 1980 and 1994
if year >= 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
# Added an else statemnet to catch any input before 1980
else:
    print("You are ancient, decrepid...a waste of skin")

# # Fix the Errors
# Needed to type convert into int
age = int(input("How old are you?"))
if age > 18:
    # it was missing an f"" and print was incorrectly indented
    print(f"You can drive at age {age}.")

# # Print is Your Friend
# Deleted useless var inits
pages = int(input("Number of pages: "))
# Deleted extra'=' in the word_per_page var
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    # This was incorrectly indented
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])