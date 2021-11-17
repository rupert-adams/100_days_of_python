############DEBUGGING TESTS#####################

number = int(input("Which number do you want to check?"))

# if statement was missing '='
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#  --------------

# 'year' var was missing int type convert
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
  print("Not leap year.")

#  --------------

for number in range(1, 101):
    # changed 'or' operator for 'and'
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # if statement turned to elif
    elif number % 3 == 0:
        print("Fizz")
    # if statement turned to elif
    elif number % 5 == 0:
        print("Buzz")
    # took number out of list
    else:
        print(number)