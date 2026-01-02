from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        #reading data from file
        with open("data.txt") as default_score:
            content=default_score.read()

        self.HighScore=int(content)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score :{self.HighScore}", align="center", font=("Arial", 20, "normal"))


    def inc(self):
        self.score+=1
        self.update_scoreboard()



    def reset_game(self):
        if self.score > self.HighScore :
            self.HighScore=self.score
            # writing data into file

            with open("data.txt",mode="w") as high_score:
                high_score.write(f"{self.HighScore}")

        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align="center", font=("Arial", 20, "normal"))






# board=Scoreboard()
# screen=Screen()
# screen.exitonclick()