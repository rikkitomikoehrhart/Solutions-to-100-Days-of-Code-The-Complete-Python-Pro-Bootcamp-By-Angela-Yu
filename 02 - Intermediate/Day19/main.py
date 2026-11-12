import turtle as turtle_module
import random

screen = turtle_module.Screen()
screen.setup(width=500, height=400)
screen.setworldcoordinates(llx=-250, lly=-200, urx=250, ury=200) 
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_start = -125
is_race_on = False

turtles = []

for color in colors:
    turtle = turtle_module.Turtle()
    turtle.penup()
    turtle.color(color)
    turtle.shape("turtle")
    turtle.goto(x=-235, y=y_start)
    y_start += 50
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle won!")
            else:
                print(f"Sorry, you lost, {winner} turtle won, not the {user_bet} turtle.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()