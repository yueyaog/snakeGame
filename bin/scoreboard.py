from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.score = score
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("red")
        self.setpos(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)





