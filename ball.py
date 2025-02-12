import turtle
import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = turtle.Screen()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x_move = random.choice([0.1, -0.1])
        self.y_move = 1
        self.move_speed = 1


    def ball_move(self):
        new_x = self.xcor() + self.x_move * self.move_speed
        new_y = self.ycor() + self.y_move * self.move_speed
        self.goto(new_x, new_y)

    def bounce(self):
        self.x_move *= -1
        self.move_speed *= 1.02

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 1.02


    def reset_position(self):
        self.goto(0, 0)
        self.x_move = random.choice([0.1, -0.1])
        self.y_move = 1
        self.move_speed = 1

