from turtle import Turtle


class Pitch(Turtle):
    def __init__(self):
        super().__init__()
        self.outer = -275
        self.top_wall = Turtle()
        self.top_wall.color("grey")
        self.top_wall.shape("square")
        self.top_wall.penup()

        self.edge_wall = Turtle()
        self.edge_wall.color("grey")
        self.edge_wall.shape("square")
        self.edge_wall.penup()

        self.opposite_wall = Turtle()
        self.opposite_wall.color("grey")
        self.opposite_wall.shape("square")
        self.opposite_wall.penup()

        self.penup()

    def pitch_top(self):
        self.top_wall.goto(x=0, y=450)
        self.top_wall.shapesize(stretch_wid=1, stretch_len=40)

    def pitch_edges(self):
        self.edge_wall.goto(x=390, y=0)
        self.edge_wall.shapesize(stretch_wid=45, stretch_len=1)

    def pitch_opposite_edges(self):
        self.opposite_wall.goto(x=-390, y=0)
        self.opposite_wall.shapesize(stretch_wid=45, stretch_len=1)



