from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
left_score=Score((-300,270))
right_score=Score((300,270))

right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))


football = Ball()



screen.update()
screen.listen()

screen.onkey(fun=right_paddle.mov_up,key="Up")
screen.onkey(fun=right_paddle.mov_down,key="Down")
screen.onkey(fun=left_paddle.mov_up,key="w")
screen.onkey(fun=left_paddle.mov_down,key="s")





tru_cond=True


while tru_cond:
    screen.update()
    time.sleep(football.mov_speed)


    football.refresh()

    #collision with wall
    if football.ycor() > 290 or football.ycor() < -290 :
        #bouncing back
        football.bounce_back()
    #collision with paddle
    if football.distance(right_paddle) < 50 and football.xcor() > 320  or football.distance(left_paddle) < 50 and football.xcor() < -320:

        football.paddle_bounce()


    if football.xcor() > 400:
        football.new_start()
        left_score.inc_score()

    if football.xcor() < -400:
        football.new_start()
        right_score.inc_score()

    #
    # # right_paddle.move()
    # if right_paddle.head.ycor()> 270 :
    #         shift = right_paddle.head
    #         right_paddle.head = right_paddle.tail
    #         right_paddle.tail = shift












screen.exitonclick()