import turtle
import time

from scoreboard import ScoreBoard
from snake import Snake
from food import Food

screen=turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

new_snake=Snake()
my_food=Food()
my_scoreboard=ScoreBoard()

screen.listen()
screen.onkey(new_snake.moveUp,"Up")
screen.onkey(new_snake.moveDown,"Down")
screen.onkey(new_snake.moveRight,"Right")
screen.onkey(new_snake.moveLeft,"Left")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    new_snake.move()

    #Detect collision with food
    if new_snake.head.distance(my_food) < 15:#check the distance between  snake object and food object
        my_food.refresh()
        my_scoreboard.increase_score()
        new_snake.extend_snake()

    #Detects collision with wall
    if new_snake.head.xcor() >290 or new_snake.head.xcor() < -290 or new_snake.head.ycor()>290 or new_snake.head.ycor()<-290:
        game_is_on=False
        my_scoreboard.game_over()

    #Detects collision with tail
    for segment in new_snake.segments[1:]:

        if new_snake.head.distance(segment)< 10:
            game_is_on=False
            my_scoreboard.game_over()



screen.exitonclick()
