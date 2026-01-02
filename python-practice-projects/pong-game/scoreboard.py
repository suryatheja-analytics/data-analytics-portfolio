from turtle import Turtle

class Score(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(pos)
        self.write(f"Score:{self.score}",align="center",font=("Arial",20,"normal"))


    def inc_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 20, "normal"))



