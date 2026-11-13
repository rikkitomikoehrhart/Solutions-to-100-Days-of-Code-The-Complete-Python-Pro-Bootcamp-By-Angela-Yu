import turtle as t_mod
from snake import Snake
import time

screen = t_mod.Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(llx=-300, lly=-300, urx=300, ury=300)
screen.bgcolor("black")
screen.title("Sssssnake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()