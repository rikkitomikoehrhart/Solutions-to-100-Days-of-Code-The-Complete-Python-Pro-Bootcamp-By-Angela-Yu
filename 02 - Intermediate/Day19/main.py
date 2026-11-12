import turtle as turtle_module
import random

screen = turtle_module.Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(-300, -300, 300, 300) 



t = turtle_module.Turtle()
def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    t.setheading(t.heading() + 10)

def turn_right():
    t.setheading(t.heading() - 10)

def clear():
    t.clear()
    t.penup
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)



screen.exitonclick()