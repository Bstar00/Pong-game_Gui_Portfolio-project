import turtle

# Set up game screen
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 20

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 20

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.0
ball.dy = -2.0

# Score
score1 = 0
score2 = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 24, "normal"))

# Function to move paddle1 up
def paddle1_up():
    y = paddle1.ycor()
    if y < 250:
        y += paddle1.dy
    paddle1.sety(y)

# Function to move paddle1 down
def paddle1_down():
    y = paddle1.ycor()
    if y > -240:
        y -= paddle1.dy
    paddle1.sety(y)

# Function to move paddle2 up
def paddle2_up():
    y = paddle2.ycor()
    if y < 250:
        y += paddle2.dy
    paddle2.sety(y)

# Function to move paddle2 down
def paddle2_down():
    y = paddle2.ycor()
    if y > -240:
        y -= paddle2.dy
    paddle2.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

# Function to update the score display
def update_score():
    score_display.clear()
    score_display.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Arial", 24, "normal"))

# Function to check paddle and ball collisions
def check_collisions():
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
        ball.color("blue")
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
        ball.color("red")
        ball.setx(-340)
        ball.dx *= -1

# Function to automatically move the paddles when the ball is in their direction
def auto_move_paddles():
    # Move the left paddle when the ball is moving towards it
    if ball.dx < 0:
        if paddle1.ycor() < ball.ycor():
            paddle1_up()
        elif paddle1.ycor() > ball.ycor():
            paddle1_down()

    # Move the right paddle when the ball is moving towards it
    if ball.dx > 0:
        if paddle2.ycor() < ball.ycor():
            paddle2_up()
        elif paddle2.ycor() > ball.ycor():
            paddle2_down()

# Set the score limit for the game over
score_limit = 5  # Change this to the desired score limit

# Function to check for game over
def check_game_over():
    global score1, score2
    if score1 >= score_limit or score2 >= score_limit:
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
        if score1 >= score_limit:
            message = "Player 1 wins!"
        else:
            message = "Player 2 wins!"
        message += "\nPlay Again? (Y/N)"
        score_display.clear()
        score_display.goto(0, 0)
        score_display.write(message, align="center", font=("Arial", 24, "normal"))

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        update_score()
        check_collisions()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        update_score()
        check_collisions()

    # Call the auto_move_paddles function
    auto_move_paddles()
