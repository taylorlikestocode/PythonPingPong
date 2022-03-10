import string
import turtle 
    #Score
score_player_1 = 0
score_player_2 = 0

    # basic game setup

game_window = turtle.Screen()
game_window.title("Ping Pong Game!") #title
game_window.bgcolor("pink") #background color
game_window.setup(width=800, height=600) #window size
game_window.tracer(0) #no auto update, manual update, game speed up

    # paddle 1

paddle1= turtle.Turtle()
paddle1.speed(0) #animation speed. 0 is fastest/highest
paddle1.shape("square") #paddle shape. can be square,circle,triangle
paddle1.color("white") #paddle color
paddle1.shapesize(stretch_wid=5, stretch_len=1) #paddle size
paddle1.penup()
paddle1.goto(-350, 0) 

    # paddle 2

paddle2= turtle.Turtle()
paddle2.speed(0) #animation speed. 0 is fastest/highest
paddle2.shape("square") #paddle shape. can be square,circle,triangle
paddle2.color("white") #paddle color
paddle2.shapesize(stretch_wid=5, stretch_len=1) #paddle size
paddle2.penup()
paddle2.goto(+350, 0) 

    # ping pong ball

ball=turtle.Turtle()
ball.speed(0) #animation speed. 0 is fastest/highest
ball.shape("circle") #ball shape. can be square,circle,triangle
ball.color("white") #ball color
ball.penup()
ball.goto(0, 0)
ball.dx= 2
ball.dy= -2

    # pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0 Player 2: 0 ", align="center", font=("Courier", 24, "normal"))
    # paddle 1 up
 
def paddle1_up(): #define function
    y = paddle1.ycor() #return y coordinate
    y += 20 # add pizedls to y coordinate
    paddle1.sety(y)

    # paddle 1 down
def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)
    
    # paddle 2 up
 
def paddle2_up(): #define function
    y = paddle2.ycor() #return y coordinate
    y += 20 # add pizedls to y coordinate
    paddle2.sety(y)

    # paddle 2 down
def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)
    
    # keyboard binding

game_window.listen() #tells program to listen for keyboad input
game_window.onkeypress(paddle1_up, "w") #assign keyboard input action up to w 
game_window.onkeypress(paddle1_down, "s") #assign keyboard input action down to s
game_window.onkeypress(paddle2_up, "Up") #assign keyboard to up arrow
game_window.onkeypress(paddle2_down, "Down") #assign keyboard to down arrow



    # main game loop
while True:
    game_window.update() #screen will be updated everytime loop runs
     
    # move ping pong ball  
    ball.setx(ball.xcor()+ball.dx) #ball starts at x cor and moves by dx value
    ball.sety(ball.ycor()+ball.dy) #ball starts at y cor and moves by dy value
    
    # border check
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy*=-1 #reverses direction upon hitting border
        
    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*=-1 
        
    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_player_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {} ".format(score_player_1, score_player_2), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_player_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {} ".format(score_player_1, score_player_2), align="center", font=("Courier", 24, "normal"))
    
    # collisions
    if ball.xcor() > 320 and ball.xcor() < 350 and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(320)
        ball.dx *= -1
    
    if ball.xcor() < -320 and ball.xcor() > -350 and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-320)
        ball.dx *= -1
        