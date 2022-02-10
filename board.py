from turtle import Turtle


class board(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
