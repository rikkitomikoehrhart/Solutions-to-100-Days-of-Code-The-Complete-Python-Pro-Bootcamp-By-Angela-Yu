import turtle as t_mod

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(t_mod.Turtle):

    def __init__(self):
        super().__init__()
        self.color("light blue")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 175)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(200, 175)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()