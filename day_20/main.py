from turtle import Screen
from snake import Snake
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

MOVEMENT_KEYS = {
    "Up": snake.up, 
    "Down": snake.down, 
    "Left": snake.left, 
    "Right": snake.right
    }

screen.listen()
for item in MOVEMENT_KEYS:
            screen.onkey(key=item, fun=MOVEMENT_KEYS[item])

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()