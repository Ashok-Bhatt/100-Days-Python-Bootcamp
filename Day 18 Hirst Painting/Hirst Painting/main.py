from colorgram import extract
from turtle import Turtle, Screen, colormode
from random import choice


def generate_hex(rgb_list):

    hex_list = []
    for color in rgb_list:
        hex_list.append(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    return hex_list


def replace_spot():

    t1.backward(gap*10)
    t1.left(90)
    t1.forward(gap)
    t1.right(90)


colormode(255)

color_obj = extract("Hirst Painting/paint3.jpg",30)
colors_rgb = [(x.rgb.r,x.rgb.b, x.rgb.r) for x in color_obj]

gap = 50

s1 = Screen()
t1 = Turtle()

t1.shape("arrow")
t1.up()
t1.hideturtle()
t1.goto(-300,-300)
t1.showturtle()

for row in range(10):
    for col in range(10):
        t1.dot(20, choice(colors_rgb))
        t1.forward(gap)
    replace_spot()

s1.exitonclick()