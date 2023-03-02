#importing the turtle library
from operator import truediv
from turtle import Turtle



import turtle

#set up game screen
turtle.setup(400,300)
#set game screen background color
turtle.bgcolor("black")

#Left Padle(Paddle 1)
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1) #make paddle wider
paddle1.penup()
paddle1.goto(-350,0)
paddle1.dy = 0
 
#Right paddle(Paddle 2)
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)
paddle2.dy = 0

#Creating the ball 
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#Game Rules
game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 3,
    "ball_speed": 3
}

#Score dispaly
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 24, "normal"))


##Game mechanics coding logic

paddle1.sety(paddle1.ycor() + paddle1.dy)
paddle2.sety(paddle2.ycor() + paddle2.dy)
ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)


# Check for game over conditions 
if points["player1"] == game_rules["max_points"]:
    game_over = True
    winner = "player1"
elif points ["player2"] == game_rules["max_points"]:
    game_over = True
winner  = "player2"

#Check for ball collision with paddles
if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
    ball.setx(340)
    ball.dx *= -1
    
     