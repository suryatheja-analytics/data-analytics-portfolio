import random
from turtle import Turtle,Screen


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x = round(random.uniform(-280.0, 280.0))
        y = round(random.uniform(-280.0, 280.0))
        self.goto(x, y)
# chick=Food()
# # chick.shape("circle")
# # x=round(random.uniform(-300.0,300.0))
# # y=round(random.uniform(-300.0,300.0))
# # chick.penup()
# # chick.
# # chick.dot()
# screen=Screen()
# screen.exitonclick()
