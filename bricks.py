import turtle
from turtle import Turtle
import random

colors = [
    "red", "green", "blue", "yellow", "white", "orange",
    "purple", "brown", "pink", "gray", "violet", "lightblue",
    "lightgreen", "lightyellow", "lightpink", "lightgray",
    "darkblue", "darkgreen", "darkred", "gold", "silver", "cyan", "magenta"
]

class Bricks:
    def __init__(self):
        self.bricks = []

    def brick(self, x, y):
        brick = Turtle()
        brick.shape("square")
        brick.color(random.choice(colors))
        brick.penup()
        brick.goto(x, y)
        brick.shapesize(stretch_wid=2, stretch_len=4)
        return brick

    def create_bricks(self):
        start_x = -320
        start_y = 380
        for row in range(12):
            for col in range(9):
                brick = self.brick(start_x + col * 80, start_y - row * 20)
                self.bricks.append(brick)

    def break_brick(self, brick):
        brick.hideturtle()
        self.bricks.remove(brick)

