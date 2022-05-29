import turtle
import os
from playsound import playsound

width,height = 800,600

# Setup
w = turtle.Screen()
w.title('Pong Sample')
w.bgcolor('black')
w.setup(width,height)
w.tracer(0)

# Paddle A
pad_A = turtle.Turtle()
pad_A.speed(0)
pad_A.shape('square')
pad_A.shapesize(5,1)
pad_A.color('white')
pad_A.up()
pad_A.goto(-350,0)

# Da ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.up()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.05

# Functions
speed = 5

def pad_A_up():
    y = pad_A.ycor()
    y += speed
    pad_A.sety(y)

def pad_A_down():
    y = pad_A.ycor()
    y -= speed
    pad_A.sety(y)

def pad_A_left():
    x = pad_A.xcor()
    x -= speed
    pad_A.setx(x)

def pad_A_right():
    x = pad_A.xcor()
    x += speed
    pad_A.setx(x)

w.listen()
w.onkeypress(pad_A_up,'w')
w.onkeypress(pad_A_down,'s')
# w.onkeypress(pad_A_left,'a')
# w.onkeypress(pad_A_right,'d')

# Score
score_player = 0

# Score record
pen = turtle.Turtle()
pen.speed(0)
turtle.colormode(255)
pen.color(151,169,84)
pen.up(); pen.ht()
pen.goto(0, 260)
pen.write('0',align='center',font=('Gang of Three',24,'normal'))

# Game loop
while True:
    w.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border-check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -0.98
        playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -0.98
        playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -0.98
        playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -0.98
        playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
    
    # Paddle-check (and also scoring)
    if abs(pad_A.xcor()-ball.xcor())<=20 and abs(pad_A.ycor()-ball.ycor())<=50:
        playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
        if ball.xcor() > pad_A.xcor():
            ball.setx(pad_A.xcor() + 22)
        else: ball.setx(pad_A.xcor() - 22)
        ball.dx *= -1.02
        score_player += 1
        pen.clear()
        pen.write(score_player,align='center',font=('Gang of Three',24,'normal'))
    
    speed += 0.0001