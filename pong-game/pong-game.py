import turtle
import winsound

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


# Keyboard bindings
wn.listen()  # Listen for keyboard input
wn.onkeypress(paddle_a_up, "w")  # Bind the "w" key to the paddle_a_up function, calling it when the key is pressed
wn.onkeypress(paddle_a_down, "s")  # Bind the "s" key to the paddle_a_down function, calling it when the key is pressed
wn.onkeypress(paddle_b_up, "Up")  # Bind the "Up" key to the paddle_b_up function, calling it when the key is pressed
wn.onkeypress(paddle_b_down, "Down")  # Bind the "Down" key to the paddle_b_down function, calling it when the key is pressed


#Main game loop
while True:
    wn.update()  # Updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Update the x-coordinate of the ball by adding the change in x (dx)
    ball.sety(ball.ycor() + ball.dy)  # Update the y-coordinate of the ball by adding the change in y (dy)

    # Border checking
    if ball.ycor() > 290: # If the ball hits the top border
        ball.sety(290)  # Set the y-coordinate of the ball to 290 (the top border)
        ball.dy *= -1  # Reverse the direction of the ball's movement in the y-axis
        winsound.PlaySound("C:\\Users\\choic\\Desktop\\pong-game\\sounds\\bounce.wav", winsound.SND_ASYNC) # Play a sound when the ball hits the border (you can replace "" with the path to a sound file)
    
    if ball.ycor() < -290: # If the ball hits the bottom border
        ball.sety(-290)  # Set the y-coordinate of the ball to -290 (the bottom border)
        ball.dy *= -1  # Reverse the direction of the ball's movement in the y-axis
        winsound.PlaySound("C:\\Users\\choic\\Desktop\\pong-game\\sounds\\bounce.wav", winsound.SND_ASYNC) # Play a sound when the ball hits the border (you can replace "" with the path to a sound file)
    
    if ball.xcor() > 390: # If the ball goes past the right border
        ball.goto(0, 0)  # Move the ball back to the center of the screen
        ball.dx *= -1  # Reverse the direction of the ball's movement in the x-axis
        score_a += 1  # Increment the score for player A
        pen.clear()  # Clear the previous score from the screen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # Update the score on the screen

    if ball.xcor() < -390: # If the ball goes past the left border
        ball.goto(0, 0)  # Move the ball back to the center of the screen
        ball.dx *= -1  # Reverse the direction of the ball's movement in the x-axis
        score_b += 1  # Increment the score for player B
        pen.clear()  # Clear the previous score from the screen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # Update the score on the screen

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40): # If the ball collides with paddle B
        ball.setx(340)  # Set the x-coordinate of the ball to 340 (the edge of paddle B)
        ball.dx *= -1  # Reverse the direction of the ball's movement in the x-axis
        winsound.PlaySound("C:\\Users\\choic\\Desktop\\pong-game\\sounds\\bounce.wav", winsound.SND_ASYNC) # Play a sound when the ball hits the paddle (you can replace "" with the path to a sound file)

    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40): # If the ball collides with paddle A
        ball.setx(-340)  # Set the x-coordinate of the ball to -340 (the edge of paddle A)
        ball.dx *= -1  # Reverse the direction of the ball's movement in the x-axis
        winsound.PlaySound("C:\\Users\\choic\\Desktop\\pong-game\\sounds\\bounce.wav", winsound.SND_ASYNC) # Play a sound when the ball hits the paddle (you can replace "" with the path to a sound file)