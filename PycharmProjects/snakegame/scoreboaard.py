from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score = {self.highscore}", font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.updatescoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", font=FONT, align=ALIGNMENT)

    def increasescore(self):
        self.score += 1
        self.updatescoreboard()


