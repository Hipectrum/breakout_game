import turtle
import paddle
from scoreboard import Scoreboard
from ball import Ball
from pitch import Pitch
from bricks import Bricks

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)

screen.tracer(0)

screen.setup(width=1280, height=1024)
screen.bgcolor("black")
screen.title("Breakout")

ballr = Ball()
scoreboard = Scoreboard()

pitch = Pitch()
paddle = paddle.Paddle((0, -360))


pitch.pitch_top()
pitch.pitch_edges()
pitch.pitch_opposite_edges()


screen.listen()
screen.onkeypress(paddle.go_left, "a")
screen.onkeypress(paddle.go_right, "d")

bricks = Bricks()
bricks.create_bricks()

is_on = True

def game():

    if is_on:
        ballr.ball_move()

        if paddle.ycor() - 10 < ballr.ycor() < paddle.ycor() + 10 and paddle.xcor() -50 < ballr.xcor() < paddle.xcor() + 50:
            ballr.sety(paddle.ycor() + 10)
            ballr.bounce_y()

            if ballr.xcor() < paddle.xcor():
                ballr.x_move = -abs(ballr.x_move)
            else:
                ballr.x_move = abs(ballr.x_move)


        if paddle.xcor() - paddle.width() / 2 < -330:
            paddle.setx(-330)

        if paddle.xcor() + paddle.width() / 2 > 330:
            paddle.setx(330)

        if ballr.ycor() > 440:
            ballr.bounce_y()

        if ballr.xcor() > 380 or ballr.xcor() < -380:
            ballr.bounce()

        def create_bricks():
            for hit in bricks.bricks:
                if hit.isvisible() and hit.ycor() - 10 < ballr.ycor() < hit.ycor() + 10\
                        and hit.xcor() - 40 < ballr.xcor() < hit.xcor() +40:
                    bricks.break_brick(hit)
                    ballr.bounce_y()
                    ballr.move_speed *= 1.02
                    scoreboard.player_points += 1
                    scoreboard.update_scoreboard()


        if ballr.ycor() < -500:
            bricks.create_bricks()
            ballr.reset_position()
            scoreboard.player_points = 0
            scoreboard.update_scoreboard()

        create_bricks()
        screen.update()
        screen.ontimer(game, 1)

game()


screen.exitonclick()