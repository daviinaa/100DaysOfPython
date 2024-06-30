from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()


screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     detect collision with top wall
    if ball.ycor() > 270 or ball.ycor() < - 270:
        ball.bounce_y()

#   detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#  add score to the l opponent if the other fails to catch the ball
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

#  add score to the r opponent if the other fails to catch the ball
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

