from turtle import Turtle, Screen

curser = Turtle()
screen = Screen()

def move_forward():
    curser.forward(10)

def move_backward():
    curser.backward(10)

def turn_clockwise():
    curser.right(10)

def turn_counterclockwise():
    curser.left(10)

def reset():
    curser.home()
    curser.clear()

INPUT_CONSTRAINT= {
    "w": move_forward,
    "s": move_backward,
    "a": turn_counterclockwise,
    "d": turn_clockwise,
    "c": reset,
}

def locomotion():
    for item in INPUT_CONSTRAINT:
        screen.onkey(key=item, fun=INPUT_CONSTRAINT[item])

screen.listen()
locomotion()
screen.exitonclick()