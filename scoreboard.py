from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x= -400, y= 460)
        self.pencolor("white")
        self.hideturtle()

        self.player_points = 0


        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.player_points}      ", align="left", font=("Courier", 24, "normal"))



    def counting_points(self):
        self.player_points += 1

        self.update_scoreboard()
