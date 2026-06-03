import turtle
import winsound
import os
import random

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
sound_file = os.path.join(script_dir, "sounds", "bounce.wav")

wn= turtle.Screen()  # Create a window for the game
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turns off screen updates

# Score
score_a = 0  # Initialize score for player A
score_b = 0  # Initialize score for player B

# Paddle A
paddle_a = turtle.Turtle() # Create a turtle object for paddle A
paddle_a.speed(0)  # Set the speed of the turtle animation to the maximum
paddle_a.shape("square")  # Set the shape of the turtle to a square
paddle_a.color("green")  # Set the color of the turtle to green
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the turtle to make it a paddle 20 pixels wide and 100 pixels tall
paddle_a.penup() # Lift the pen up so it doesn't draw when moving
paddle_a.goto(-350, 0)  # Move the turtle to the left side of the screen

# Paddle B
paddle_b = turtle.Turtle() # Create a turtle object for paddle B
paddle_b.speed(0)  # Set the speed of the turtle animation to the maximum
paddle_b.shape("square")  # Set the shape of the turtle to a square
paddle_b.color("blue")  # Set the color of the turtle to blue
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the turtle to make it a paddle 20 pixels wide and 100 pixels tall
paddle_b.penup() # Lift the pen up so it doesn't draw when moving
paddle_b.goto(350, 0)  # Move the turtle to the right side of the screen


# Ball
ball = turtle.Turtle() # Create a turtle object for the ball
ball.speed(0)  # Set the speed of the turtle animation to the maximum
ball.shape("circle")  # Set the shape of the turtle to a circle
ball.color("red")  # Set the color of the turtle to red
ball.penup() # Lift the pen up so it doesn't draw when moving
ball.goto(0, 0)  # Move the turtle to the center of the screen
ball.dx = 0.08 # Set the change in x-coordinate for the ball's movement
ball.dy = 0.08 # Set the change in y-coordinate for the ball's movement

# Pen
pen = turtle.Turtle() # Create a turtle object for the pen
pen.speed(0)  # Set the speed of the turtle animation to the maximum
pen.color("white")  # Set the color of the turtle to white
pen.penup() # Lift the pen up so it doesn't draw when moving
pen.hideturtle() # Hide the turtle shape
pen.goto(0, 260)  # Move the turtle to the top center of the screen
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")) # Write the initial score on the screen

# Game mode selection
mode_text = turtle.Turtle()
mode_text.speed(0)
mode_text.color("yellow")
mode_text.penup()
mode_text.hideturtle()
mode_text.goto(0, -260)
mode_text.write("Press 1 for Single Player (vs AI) or 2 for Two Player", align="center", font=("Courier", 12, "normal"))

game_mode = None  # Will be set to "single" or "two_player"
game_over = False  # Track if the game is over
WIN_SCORE = 10  # Score needed to win

def set_single_player():
    global game_mode, game_over, score_a, score_b
    game_mode = "single"
    game_over = False
    score_a = 0  # Reset scores
    score_b = 0
    ball.goto(0, 0)  # Reset ball position
    ball.dx = 0.08
    ball.dy = 0.08
    paddle_a.goto(-350, 0)  # Reset paddle positions
    paddle_b.goto(350, 0)
    pen.clear()
    pen.goto(0, 260)
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    mode_text.clear()
    mode_text.goto(0, -260)
    mode_text.write("Single Player Mode - Press W/S to move", align="center", font=("Courier", 12, "normal"))

def set_two_player():
    global game_mode, game_over, score_a, score_b
    game_mode = "two_player"
    game_over = False
    score_a = 0  # Reset scores
    score_b = 0
    ball.goto(0, 0)  # Reset ball position
    ball.dx = 0.08
    ball.dy = 0.08
    paddle_a.goto(-350, 0)  # Reset paddle positions
    paddle_b.goto(350, 0)
    pen.clear()
    pen.goto(0, 260)
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    mode_text.clear()
    mode_text.goto(0, -260)
    mode_text.write("Two Player Mode", align="center", font=("Courier", 12, "normal"))

def display_winner(winner):
    """Display the winner message"""
    mode_text.clear()
    mode_text.goto(0, -260)
    mode_text.write(f"{winner} WINS! Press 1 or 2 to play again", align="center", font=("Courier", 14, "normal"))
    pen.goto(0, 0)
    pen.clear()
    pen.write(f"Game Over! {winner} Wins!", align="center", font=("Courier", 32, "bold"))

# Bind mode selection keys
wn.listen()
wn.onkeypress(set_single_player, "1")
wn.onkeypress(set_two_player, "2")


# Functions to move the paddles
def paddle_a_up():
    y  = paddle_a.ycor()  # Get the current y-coordinate of paddle A
    y += 20 # Increase the y-coordinate by 20 pixels
    paddle_a.sety(y)  # Set the new y-coordinate of paddle A

def paddle_a_down():
    y  = paddle_a.ycor()  # Get the current y-coordinate of paddle A
    y -= 20 # Decrease the y-coordinate by 20 pixels
    paddle_a.sety(y)  # Set the new y-coordinate of paddle A

def paddle_b_up():
    y  = paddle_b.ycor()  # Get the current y-coordinate of paddle B
    y += 20 # Increase the y-coordinate by 20 pixels
    paddle_b.sety(y)  # Set the new y-coordinate of paddle B

def paddle_b_down():
    y  = paddle_b.ycor()  # Get the current y-coordinate of paddle B
    y -= 20 # Decrease the y-coordinate by 20 pixels
    paddle_b.sety(y)  # Set the new y-coordinate of paddle B

def ai_move():
    """AI opponent logic - moves paddle B to follow the ball"""
    paddle_center = paddle_b.ycor()
    ball_y = ball.ycor()
    
    # Only move AI if ball is moving towards it (positive dx)
    if ball.dx > 0:
        # Add slight imperfection to make AI beatable (80% accuracy)
        if random.random() < 0.65:  # 65% chance to move towards the ball
            if ball_y > paddle_center + 5:
                paddle_b_up()
            elif ball_y < paddle_center - 5:
                paddle_b_down()

# Keyboard bindings
wn.listen()  # Listen for keyboard input
wn.onkeypress(paddle_a_up, "w")  # Bind the "w" key to the paddle_a_up function
wn.onkeypress(paddle_a_down, "s")  # Bind the "s" key to the paddle_a_down function
wn.onkeypress(paddle_b_up, "Up")  # Bind the "Up" key to move paddle B (two-player only)
wn.onkeypress(paddle_b_down, "Down")  # Bind the "Down" key to move paddle B (two-player only)


#Main game loop
while True:
    wn.update()  # Updates the screen
    
    # Wait for game mode selection
    if game_mode is None:
        continue
    
    # Stop all game logic if game is over
    if game_over:
        continue

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Update the x-coordinate of the ball by adding the change in x (dx)
    ball.sety(ball.ycor() + ball.dy)  # Update the y-coordinate of the ball by adding the change in y (dy)
    
    # AI opponent in single-player mode
    if game_mode == "single":
        ai_move()

    # Border checking
    if ball.ycor() > 290: # If the ball hits the top border
        ball.sety(290)  # Set the y-coordinate of the ball to 290 (the top border)
        ball.dy *= -1  # Reverse the direction of the ball's movement in the y-axis
        winsound.PlaySound(sound_file, winsound.SND_ASYNC) # Play a sound when the ball hits the border (you can replace "" with the path to a sound file)
    
    if ball.ycor() < -290: # If the ball hits the bottom border
        ball.sety(-290)  # Set the y-coordinate of the ball to -290 (the bottom border)
        ball.dy *= -1  # Reverse the direction of the ball's movement in the y-axis
        winsound.PlaySound(sound_file, winsound.SND_ASYNC) # Play a sound when the ball hits the border (you can replace "" with the path to a sound file)
    
    if ball.xcor() > 390: # If the ball goes past the right border
        ball.goto(0, 0)  # Move the ball back to the center of the screen
        ball.dx *= -1  # Reverse the direction of the ball's movement in the x-axis
        score_a += 1  # Increment the score for player A
        pen.clear()  # Clear the previous score from the screen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # Update the score on the screen
        
        # Check if player A wins
        if score_a >= WIN_SCORE:
            game_over = True
            display_winner("Player A")

    if ball.xcor() < -390: # If the ball goes past the left border
        ball.goto(0, 0)  # Move the ball back to the center of the screen
        ball.dx *= -1  # Reverse the direction of the ball's movement in the x-axis
        score_b += 1  # Increment the score for player B
        pen.clear()  # Clear the previous score from the screen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # Update the score on the screen
        
        # Check if player B wins
        if score_b >= WIN_SCORE:
            game_over = True
            display_winner("Player B" if game_mode == "two_player" else "AI")

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40): # If the ball collides with paddle B
        ball.setx(340)  # Set the x-coordinate of the ball to 340 (the edge of paddle B)
        ball.dx *= -1.02  # Reverse the direction of the ball's movement in the x-axis, increase the speed
        winsound.PlaySound(sound_file, winsound.SND_ASYNC) # Play a sound when the ball hits the paddle (you can replace "" with the path to a sound file)

    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40): # If the ball collides with paddle A
        ball.setx(-340)  # Set the x-coordinate of the ball to -340 (the edge of paddle A)
        ball.dx *= -1.02  # Reverse the direction of the ball's movement in the x-axis, increase the speed
        winsound.PlaySound(sound_file, winsound.SND_ASYNC) # Play a sound when the ball hits the paddle (you can replace "" with the path to a sound file)