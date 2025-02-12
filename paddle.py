import turtle
from turtle import Turtle

move_distance = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.screen = turtle.Screen()
        self.position = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)


    def move_paddle(self):

        self.goto(self.position)
        self.forward(move_distance)

    def collide_ball(self, ball):
        if self.distance(ball) < 100:
            return True
        return False

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())





