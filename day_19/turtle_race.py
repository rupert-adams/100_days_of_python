from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
num=-100
turtles_all_the_way_down = []

for turt_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turt_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=num)
    num+=30
    turtles_all_the_way_down.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in turtles_all_the_way_down:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"Congratulations! {user_bet} won the race!")
            else:
                print(f"Oh no, I hope you didn't put any money in {user_bet}, as {winning_colour} was the winner...")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
