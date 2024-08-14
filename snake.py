import time
from turtle import Screen, Turtle
up=90
left=180
down=270
right=0
class Snake:
    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snakes = []
        self.create_snake()
        self.head=self.snakes[0]

    def create_snake(self):
        for pos in self.positions:
           self.add_snake(pos)

    def add_snake(self,pos):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.snakes.append(snake)

    def extend(self):
        #extending the snake
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for s in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[s - 1].xcor()
            new_y = self.snakes[s - 1].ycor()
            self.snakes[s].goto(new_x, new_y)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)

    def move_left(self):
        if self.head.heading()!=right:
           self.head.setheading(left)

    def move_downward(self):
        if self.head.heading()!=up:
            self.head.setheading(down)

    def move_right(self):
        if self.head.heading()!=left:
            self.head.setheading(0)




