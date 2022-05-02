from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {
    "up": 90,
    "down": 270,
    "left": 180,
    "right": 0
}

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS["down"]:
            self.head.setheading(DIRECTIONS["up"])

    def down(self):
        if self.head.heading() != DIRECTIONS["up"]:
            self.head.setheading(DIRECTIONS["down"])

    def left(self):
        if self.head.heading() != DIRECTIONS["right"]:
            self.head.setheading(DIRECTIONS["left"])

    def right(self):
        if self.head.heading() != DIRECTIONS["left"]:
            self.head.setheading(DIRECTIONS["right"])
