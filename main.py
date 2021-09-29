from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
bouncy_ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "Left")
my_screen.onkey(l_paddle.go_down, "Right")


is_on = True

while is_on:
    time.sleep(bouncy_ball.move_speed)
    my_screen.update()
    bouncy_ball.move()
#  detect ball collision w/ wall
    if bouncy_ball.ycor() > 280 or bouncy_ball.ycor() < -280:
        bouncy_ball.bounce_y()

# detect collision w/ right paddle
    if bouncy_ball.distance(r_paddle) < 50 and bouncy_ball.xcor() > 320 or bouncy_ball.distance(l_paddle) < 50 and bouncy_ball.xcor() < -320:
        bouncy_ball.bounce_x()

# detect when right paddle misses
    if bouncy_ball.xcor() > 380:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        bouncy_ball.reset_position()

    # left paddle misses
    if bouncy_ball.xcor() < -380:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        bouncy_ball.reset_position()










my_screen.exitonclick()