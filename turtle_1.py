#turtle graphics
import turtle
from turtle import *

width = 500
height = 500
DELAY = 20 

def move_turt():
    my_turtle.forward(1)
    my_turtle.right(2)
    screen.update()
    screen.ontimer(move_turt, DELAY)

screen = turtle.Screen()
screen.setup(width,height)
screen.title("Turtle")
screen.bgcolor("cyan")
screen.tracer(0)  #Turns off the automatic animation

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

move_turt()

turtle.done()