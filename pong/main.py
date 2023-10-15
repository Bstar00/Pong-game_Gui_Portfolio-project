import turtle
import time

# Set up the game screen
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Paddle settings
paddle_speed = 20
paddle_width = 5
paddle_height = 1

# Create Paddle class
class Paddle(turtle.Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=paddle_width, stretch_len=paddle_height)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        y = self.ycor()
        if y < 250:
            y += paddle_speed
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        if y > -240:
            y -= paddle_speed
        self.sety(y)

# Create paddles
paddle1 = Paddle("red", -350, 0)
paddle2 = Paddle("blue", 350, 0)

# Ball settings
ball_speed = 2.0
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed
ball.dy = -ball_speed

# Score
score1 = 0
score2 = 0

# Score display settings
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 24, "normal"))

# Function to update the score display
def update_score():
    score_display.clear()
    score_display.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Arial", 24, "normal"))

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle1.move_up, "w")
wn.onkeypress(paddle1.move_down, "s")
wn.onkeypress(paddle2.move_up, "Up")
wn.onkeypress(paddle2.move_down, "Down")

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
    if ball.dx < 0:
        if paddle1.ycor() < ball.ycor():
            paddle1.move_up()
        elif paddle1.ycor() > ball.ycor():
            paddle1.move_down()

    if ball.dx > 0:
        if paddle2.ycor() < ball.ycor():
            paddle2.move_up()
        elif paddle2.ycor() > ball.ycor():
            paddle2.move_down()

# Set the score limit for the game over
score_limit = 5

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

        # Wait for user input to play again
        wn.onkeypress(restart_game, "y")
        wn.onkeypress(quit_game, "n")

# Function to restart the game
def restart_game():
    global score1, score2
    score1 = 0
    score2 = 0
    update_score()
    ball.goto(0, 0)
    ball.dx = ball_speed
    ball.dy = -ball_speed
    score_display.clear()
    wn.onkeypress(paddle1.move_up, "w")
    wn.onkeypress(paddle1.move_down, "s")
    wn.onkeypress(paddle2.move_up, "Up")
    wn.onkeypress(paddle2.move_down, "Down")
    check_game_over()

# Function to quit the game
def quit_game():
    wn.bye()

# Main game loop
def game_loop():
    global score1, score2 
    wn.update()
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
        check_game_over()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        update_score()
        check_collisions()
        check_game_over()

    # Call the auto_move_paddles function
    auto_move_paddles()

    # Set the game loop to run again
    wn.ontimer(game_loop, 10)  # Delay in milliseconds

# Start the game loop
game_loop()

# Start the game
wn.mainloop()
