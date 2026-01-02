from turtle import Turtle

import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(1, 1)
        self.x_move=10
        self.y_move=10
        self.mov_speed=0.1
        # self.goto(380,280)

    def refresh(self):

        x_new=self.xcor() + self.x_move
        y_new=self.ycor() + self.y_move
        # self.speed("slowest")
        self.goto(x_new,y_new)

    #top and bottom bounces
    def bounce_back(self):
        self.y_move *= -1

    #paddlebounces
    def paddle_bounce(self):
        self.x_move *= -1
        self.mov_speed *= 0.9




    def new_start(self):
        self.goto(0,0)
        self.paddle_bounce()
        self.mov_speed = 0.1













    #     self.basketball((380, 270))
    #
    #
    # def basketball(self,pos):
    #     rugby=Ball()
    #     rugby.shape("circle")
    #     rugby.color("red")
    #     rugby.shapesize(1,1)
    #     rugby.goto(pos)

