from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboaard import Score

screen = Screen()

#  setting up the screen color, tittle and dimension
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#  assigning objects to the class
snake = Snake()
food = Food()
score = Score()

# assigning keys to the snake movement using methods created in the snake class
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#   detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increasescore()

#  detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

#  detect collision with tail
    for segment in snake.main_seg[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
