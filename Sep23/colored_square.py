from turtle import *
import sys


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


four_color_square(int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

