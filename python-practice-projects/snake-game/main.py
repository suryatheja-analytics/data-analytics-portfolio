from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

my_snake=Snake()
food=Food()
score = Scoreboard()





my_screen.listen()
my_screen.onkey(my_snake.up,"Up")
my_screen.onkey(my_snake.down,"Down")
my_screen.onkey(my_snake.left,"Left")
my_screen.onkey(my_snake.right,"Right")

true_cond = True
while true_cond:
    my_screen.update()

    time.sleep(0.1)
    my_snake.snake_move()
    #detect collision with food
    if my_snake.head.distance(food) < 15 :

        food.refresh()
        my_snake.tail_increase()
        score.inc()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:

        score.reset_game()
        my_snake.snake_reset()

    # for segments in my_snake.segments:
    #     if segments == my_snake.head:
    #         pass
    #     elif my_snake.head.distance(segments) < 10:
    #         true_cond=False
    #         score.game_over()
    for segments in my_snake.segments[1:]:
        if my_snake.head.distance(segments) < 10 :

            score.reset_game()
            my_snake.snake_reset()

# my_screen.update()


#
# True_cond=True
# while True_cond:
#     my_screen.update()
#     time.sleep(0.1)
#
#     for segments in range(len(objects)-1,0,-1):
#         new_x=objects[segments-1].xcor()
#         new_y=objects[segments-1].ycor()
#         objects[segments].goto(new_x,new_y)
#
#
#     objects[0].forward(20)
#     my_screen.onkey(key="a",fun=move_left)
#


    # my_screen.onkey(key="a", fun=move_left)



# obj_1=Turtle("square")
# obj_2=Turtle("square")
# obj_3=Turtle("square")
# obj_1.color("white")
# obj_2.color("white")
# obj_3.color("white")
#
#
# obj_2.setposition(-20,0)
# obj_3.setposition(-40,0)









my_screen.exitonclick()