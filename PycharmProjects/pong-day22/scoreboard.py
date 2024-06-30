from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.r_score, font=FONT, align=ALIGNMENT)
        self.goto(100, 200)
        self.write(self.l_score, font=FONT, align=ALIGNMENT)

    def l_point(self):
        self.l_score += 1
        self.updatescore()

    def r_point(self):
        self.r_score += 1
        self.updatescore()
