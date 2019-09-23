from turtle import *


def four_color_square(size, color1, color2, color3, color4):
    screen = Screen()
    braxton = Turtle()
    braxton.color(color1)
    braxton.forward(size)
    braxton.left(90)
    braxton.color(color2)
    braxton.forward(size)
    braxton.left(90)
    braxton.color(color3)
    braxton.forward(size)
    braxton.left(90)
    braxton.color(color4)
    braxton.forward(size)
    braxton.left(90)
    screen.exitonclick()


size = int(input("What size do you want it?: "))
color1 = input("What do you want the first color to be?: ")
color2 = input("What do you want the second color to be?: ")
color3 = input("What do you want the third color to be?: ")
color4 = input("What do you want the fourth color to be?: ")
four_color_square(size, color1, color2, color3, color4)
