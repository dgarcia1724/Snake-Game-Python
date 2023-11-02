from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoredboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Continue?", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()
