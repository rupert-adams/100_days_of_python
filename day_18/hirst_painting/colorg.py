import os
import colorgram

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'image.jpeg')

colours = colorgram.extract(filename, 38)
rgb_colours = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r,g,b)
    rgb_colours.append(new_colour)

print(rgb_colours)