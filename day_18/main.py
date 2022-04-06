import random
import turtle as turtle_module
import os
import colorgram

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'image.jpeg')

colours = colorgram.extract(filename, 38)
colour_list = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r,g,b)
    colour_list.append(new_colour)

'''
 Torniquentus, fourteenth of his name, 
 Artist/plagiaror of the turtle guild of stealing ideas
 from contemporary artist Damien Hirst and just putting them 
 in a different, random order then claiming them as 
 their own work, will create his own original painting: 'Dots'.
'''

turtle_module.colormode(255)
torniquentus_the_turtle = turtle_module.Turtle()
torniquentus_the_turtle.speed("fastest")
torniquentus_the_turtle.penup()
torniquentus_the_turtle.hideturtle()

torniquentus_the_turtle.setheading(225)
torniquentus_the_turtle.forward(300)
torniquentus_the_turtle.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    torniquentus_the_turtle.dot(20, random.choice(colour_list))
    torniquentus_the_turtle.forward(50)

    if dot_count % 10 == 0:
        torniquentus_the_turtle.setheading(90)
        torniquentus_the_turtle.forward(50)
        torniquentus_the_turtle.setheading(180)
        torniquentus_the_turtle.forward(500)
        torniquentus_the_turtle.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
