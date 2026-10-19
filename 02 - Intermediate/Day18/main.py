import turtle
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(-300, -300, 300, 300) 

turt = turtle.Turtle()
turt.shape("turtle")
turt.color("deep pink")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
turt.pensize(5)
turt.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turt.color(random_color())
        turt.circle(100)
        turt.setheading(turt.heading() + size_of_gap)

draw_spirograph(5)



screen.exitonclick()

