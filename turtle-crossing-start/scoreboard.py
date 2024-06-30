from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.pu()
        self.hideturtle()
        self.level = 0
        self.increaselevel()

    def increaselevel(self):
        self.clear()
        self.level += 1
        self.goto(-240, 270)
        self.write(f"LEVEL: {self.level}", font=FONT, align="center")

    def gameover(self):
        self.color("black")
        self.pu()
        self.hideturtle()
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=FONT, align="center")




