#Import turtle for graphical interface
import turtle

#Create a window
window = turtle.Screen()
window.title("Pong by Conor")
window.bgcolor("black")
window.setup(width=800, height=600)
#Prevent manual window updates to enable control of the speed of the game
window.tracer(0)

#Score
scoreA = 0
scoreB = 0

#Paddle A- create turtle object
paddleA = turtle.Turtle()
#Animatipn speed
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
#Control paddle length/width
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle B
paddleB = turtle.Turtle()
#Animatipn speed
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
#Control paddle length/width
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle()
#Animatipn speed
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#Seperate ball movements into x and y
ball.dx = 2
ball.dy = 2

#Pen- create a pen to keep a visual score tally
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


#Functions
def paddleAUp():
    #y coordinate returned from turtle module
    y = paddleA.ycor()
    #add 20 pixels of movement to y
    y += 20
    paddleA.sety(y)

def paddleADown():
    #y coordinate returned from turtle module
    y = paddleA.ycor()
    #add 20 pixels of movement to y
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    #y coordinate returned from turtle module
    y = paddleB.ycor()
    #add 20 pixels of movement to y
    y += 20
    paddleB.sety(y)

def paddleBDown():
    #y coordinate returned from turtle module
    y = paddleB.ycor()
    #add 20 pixels of movement to y
    y -= 20
    paddleB.sety(y)

#Keyboard binding - listen for keyboard inputs
window.listen()
window.onkeypress(paddleAUp, "w") #Press 'w' to move paddle up
window.onkeypress(paddleADown, "s") #Press 's' to move paddle down
window.onkeypress(paddleBUp, "Up") #Press 'up key' to move paddle up
window.onkeypress(paddleBDown, "Down") #Press 'down key' to move paddle down

#Main game loop
while True:
    #Update screen for every time the loop runs
    window.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking- bounce the ball off the window edges
    #Window = 600px. Half of 600px = 300. Ball = 20px. Half of ball = 10px. 300-10 = 290px.
    #Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse direction of ball

    #Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reverse direction of ball

    #Left border
    # Window = 800px. Half of 800px = 400. Ball = 20px. Half of ball = 10px. 400-10 = 390px.
    if ball.xcor() > 390:
        #Centre ball and reverse its direction
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        #Clear previous score
        pen.clear()
        #Update score
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    # Right border
    if ball.xcor() < -390:
        # Centre ball and reverse its direction
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        # Clear previous score
        pen.clear()
        #Update score
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collision- paddle B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40):
        ball.setx(340)
        #Reverse ball direction
        ball.dx *= -1

    #Paddle and ball collision- paddle A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -40):
        ball.setx(-340)
        #Reverse ball direction
        ball.dx *= -1

