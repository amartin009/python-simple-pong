# Simple Pong in Python 3
# By @AudraMartin

import turtle

wn = turtle.Screen()
wn.title("Pong by Audra Martin")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)       # sets speed to maximum speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)       # sets speed to maximum speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)       # sets speed to maximum speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)        # sets animation speed
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()                             # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")         # when user presses "w"
wn.onkeypress(paddle_a_down, "s")       # when user presses "s"
wn.onkeypress(paddle_b_up, "Up")        # when user presses "Up" arrow
wn.onkeypress(paddle_b_down, "Down")    # when user presses "Down" arrow


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking: Top and Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1                   # reverse direction of ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1                   # reverse direction of ball

    # Border Checking: Left and Right
    if ball.xcor() > 390:
        ball.goto(0, 0)                 # reset ball back to center
        ball.dx *= -1
        score_a += 1                    # increment player A score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)                  # reset ball back to center
        ball.dx *= -1
        score_b += 1                     # increment player B score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.dx *= -1
