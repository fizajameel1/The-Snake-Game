#snakegame
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen=Screen()
screen.setup(width=600,height=600) 
screen.bgcolor("black")
screen.title("The Snack Game")
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_downward,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")
game_on=True 
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #detect collisions with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    #detect collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        game_on=False
        score.game_over()

    #detect collisions with tail
    for s in snake.snakes[1:]:
        
        if snake.head.distance(s)<10:
            game_on=False 
            score.game_over()


screen.exitonclick()


