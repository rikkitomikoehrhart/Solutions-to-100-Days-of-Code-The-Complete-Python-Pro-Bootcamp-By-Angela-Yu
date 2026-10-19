import turtle as turtle_module
import random
import colors

screen = turtle_module.Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(-300, -300, 300, 300) 
turtle_module.colormode(255)

t = turtle_module.Turtle()

# Move to start
t.penup()


def draw_row(x, y):
    t.goto(x, y)
    for _ in range(10):
        t.dot(20, random.choice(colors.colors))
        t.forward(50)

x = -225
y = -250

for _ in range(10):
    draw_row(x, y)
    y += 50

screen.exitonclick()
