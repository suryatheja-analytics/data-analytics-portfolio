from turtle import Turtle,Screen
STARTIN_POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
MOVE_DIST=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head =self.segments[0]


    def create_snake(self):
        for position in STARTIN_POSITIONS:
            self.add_segment(position)


    def snake_reset(self):
        for segments in self.segments:
            segments.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self,pos):
        seg_new = Turtle("square")
        seg_new.color("white")
        # seg_new.pencolor("white")
        seg_new.penup()
        seg_new.goto(pos)
        self.segments.append(seg_new)

    def tail_increase(self):
        self.add_segment(self.segments[-1].position())


    def snake_move(self):

            for segments in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[segments - 1].xcor()
                new_y = self.segments[segments - 1].ycor()
                self.segments[segments].goto(new_x, new_y)
            self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
         if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # my_screen = Screen()
    # my_screen.setup(width=600, height=600)
    # my_screen.bgcolor("black")
    # my_screen.title("Snake Game")
    # x = 0.0
    # y = 0.0
    # objects = []

    # my_screen.exitonclick()
    # def move(self):
    #     objects[0].forward(20)