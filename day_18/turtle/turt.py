from turtle import Turtle, Screen
from random import randint, sample, choice, randrange

screen = Screen()
screen.colormode(255)

titanius_the_turtle = Turtle()
titanius_the_turtle.shape("turtle")
titanius_the_turtle.color("red")

'''
 Titanius, first of his name, 
 grand inquisitor of the great albeit slow journey 
 will walk in a square.
'''

counter = 0
square = 4

while counter != square:
    titanius_the_turtle.forward(100)
    titanius_the_turtle.left(90)
    counter+=1

# reset
titanius_the_turtle.clear()

'''
 Titanius, first of his name, 
 grand inquisitor of the great albeit slow journey 
 will walk in a dashed line.
'''

for _ in range(15):
    titanius_the_turtle.forward(10)
    titanius_the_turtle.penup()
    titanius_the_turtle.forward(10)
    titanius_the_turtle.pendown()

# reset
titanius_the_turtle.right(180)
titanius_the_turtle.forward(250)
titanius_the_turtle.clear()

'''
 Titanius, first of his name, 
 grand inquisitor of the great albeit slow journey 
 will walk in a triangle, square, pentagon, hexagon, 
 heptagon, octagon, nonagon and decagon.
'''

SHAPE_SIDES_REF = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10
}

shapes_keys = list(SHAPE_SIDES_REF.keys())

for shape in shapes_keys:
    angle = 360 / SHAPE_SIDES_REF[shape]
    for _ in range(SHAPE_SIDES_REF[shape]):
        titanius_the_turtle.forward(100)
        titanius_the_turtle.right(angle)

# reset
titanius_the_turtle.forward(50)
titanius_the_turtle.clear()

'''
 Titanius, first of his name, 
 grand inquisitor of the great albeit slow journey 
 will walk in a random line, chaning to a random colour
 unbound to the whims of man.
'''

movement_int_list = []
heading = [0, 90, 180, 270]
limit = randint(10, 100)

for _ in range(limit):
    num = randint(1, 100)
    movement_int_list.append(num)

for _ in range(randint(1,100)):
    distance = sample(movement_int_list, 1)
    direction = choice(heading)
    colour = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    titanius_the_turtle.color(colour)
    titanius_the_turtle.forward(distance[0])
    titanius_the_turtle.setheading(direction)

# reset
titanius_the_turtle.clear()
titanius_the_turtle.reset()

'''
 Titanius, first of his name, 
 grand inquisitor of the great albeit slow journey 
 will create a spirograph with random colours, 
 the sacred shape of the turtles.
'''

def draw_spirograph(size_of_gap):
    titanius_the_turtle.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        colour = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
        titanius_the_turtle.color(colour)
        titanius_the_turtle.circle(100)
        titanius_the_turtle.setheading(titanius_the_turtle.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()