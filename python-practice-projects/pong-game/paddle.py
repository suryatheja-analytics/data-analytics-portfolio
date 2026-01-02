from turtle import Turtle


class Paddle(Turtle):
        def __init__(self,pos):
            super().__init__()
            self.shape("square")
            self.penup()
            self.color("white")
            self.shapesize(5, 1)
            self.goto(pos)



        def mov_up(self):
            new_ycor=self.ycor() + 20
            if new_ycor > 260 or new_ycor < -260 :
                pass
            else:
                self.goto(self.xcor(),new_ycor)

        def mov_down(self):
            new_ycor=self.ycor() - 20
            if new_ycor > 260 or new_ycor < -260 :
                pass
            else:
                self.goto(self.xcor(),new_ycor)



