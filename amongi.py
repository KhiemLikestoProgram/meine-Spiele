import random as rd
import turtle, time
from playsound import playsound

def isfloat(*strs: str):
    for str in strs:
        try:
            float(str)
        except ValueError:
            return False
    return True

# TODO add w.textinput() in # Setup

# Variables
point = 0; times = 0; run = False; rainbow = 0
colors = [(241,52,52),(238,131,37),(252,236,50),(96,199,86),(37,247,181),(81,145,213),(98,77,238),(234,97,241),(240,63,131)]
numbatoshowdevil = 666; r1,g1,b1 = 255,255,255

# Setup
w = turtle.Screen()
w.title('Pong Sample')
w.bgcolor('black')
w.setup(1.0,1.0,None,None)
w.tracer(0)
turtle.colormode(255)

# Button
button = turtle.Turtle()
button.speed(0)
button.shape('square')
button.fillcolor('black')
button.pencolor('white')
button.shapesize(1,2,3)
button.up()
button.home()

# Border (illustration purposes only)
border = turtle.Turtle()
border.speed(0)
border.shape('square')
border.fillcolor('black')
border.pencolor('white')
border.shapesize(27.5,30,8)
border.up()
border.home()

# Da ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.turtlesize(1,1,5)
ball.fillcolor('black')
ball.pencolor(colors[rainbow])
ball.up()
ball.home()
ball.dx = 1
ball.dy = 1

# Da Ball 2
ball2 = turtle.Turtle();ball2.speed(0);ball2.shape('square');ball2.color(r1,g1,b1); ball2.up(); ball2.home()
ball2.dx = 1.1
ball2.dy = 1.1

# Functions

w.listen()
w.onkeypress(ball.ht,'h')
w.onkeypress(ball.st,'s')

# Score
score_player = 0
pen = turtle.Turtle(); pen1 = turtle.Turtle()
pen.speed(0)
pen.color(151,169,84)
pen.up(); pen.ht()
pen.goto(0,320)
pen.write('0',align='center',font=('Gang of Three',36,'normal'))
pen1.speed(0)
pen1.color(255,211,54)
pen1.up(); pen1.ht()
pen1.goto(-560,320)
pen1.write('0',align='center',font=('Gang of Three',36,'normal'))

# Game loop
while 1:
    
    w.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ball2.setx(ball2.xcor() + ball2.dx**3)
    ball2.sety(ball2.ycor() + ball2.dy**3)
    
    # Border-check
    if ball.ycor() > 260:
        point += 1; times += 1; rainbow += 1; ball2.dx = 1.1; ball2.dy = 1.1
        ball.pencolor(colors[rainbow % 8])
        ball.sety(260)
        ball.dy *= -1.01
        score_player += point
        pen.clear(); pen1.clear()
        pen.write(score_player,align='center',font=('Gang of Three',36,'normal'))
        pen1.write(times,align='left',font=('Gang of Three',36,'normal'))
        if score_player == numbatoshowdevil:
            border.pencolor(colors[0])
            playsound('D:\Programming\My programs\sounds\devillaugh.mp3',False)
        else:
            border.pencolor('white')
            playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
    if ball.ycor() < -260:
        point += 1; times += 1; rainbow += 1; ball2.dx = 1.1; ball2.dy = 1.1
        ball.pencolor(colors[rainbow % 8])
        ball.sety(-260)
        ball.dy *= -1.01
        score_player += point
        pen.clear(); pen1.clear()
        pen.write(score_player,align='center',font=('Gang of Three',36,'normal'))
        pen1.write(times,align='left',font=('Gang of Three',36,'normal'))
        if score_player == numbatoshowdevil:
            border.pencolor(colors[0])
            playsound('D:\Programming\My programs\sounds\devillaugh.mp3',False)
        else:
            border.pencolor('white')
            playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
    if ball.xcor() > 285:
        point += 1; times += 1; rainbow += 1; ball2.dx = 1.1; ball2.dy = 1.1
        ball.pencolor(colors[rainbow % 8])
        ball.setx(285)
        ball.dx *= -1.01
        score_player += point
        pen.clear(); pen1.clear()
        pen.write(score_player,align='center',font=('Gang of Three',36,'normal'))
        pen1.write(times,align='left',font=('Gang of Three',36,'normal'))
        if score_player == numbatoshowdevil:
            border.pencolor(colors[0])
            playsound('D:\Programming\My programs\sounds\devillaugh.mp3',False)
        else:
            border.pencolor('white')
            playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
    if ball.xcor() < -285:
        point += 1; times += 1; rainbow += 1; ball2.dx = 1.1; ball2.dy = 1.1
        ball.pencolor(colors[rainbow % 8])
        ball.setx(-285)
        ball.dx *= -1.01
        score_player += point
        pen.clear(); pen1.clear()
        pen.write(score_player,align='center',font=('Gang of Three',36,'normal'))
        pen1.write(times,align='left',font=('Gang of Three',36,'normal'))
        if score_player == numbatoshowdevil:
            border.pencolor(colors[0])
            playsound('D:\Programming\My programs\sounds\devillaugh.mp3',False)
        else:
            border.pencolor('white')
            playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
    if times % 2 != 1:
        if ball2.ycor() > 260:
            times += 0.5
            ball2.sety(260)
            ball2.dy *= -1.01
            pen1.clear()
            pen1.write(times,align='left',font=('Gang of Three',36,'normal'))
            playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
            r1 -= 5; g1 -= 2; b1 -= 1
            ball2.color(abs(r1)%255,abs(g1)%255,abs(b1)%255)
        if ball2.ycor() < -260:
            times += 0.5
            ball2.sety(-260)
            ball2.dy *= -1.01
            pen1.clear()
            pen1.write(times,align='left',font=('Gang of Three',36,'normal'))
            playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
            r1 -= 1; g1 -= 5; b1 -= 2
            ball2.color(abs(r1)%255,abs(g1)%255,abs(b1)%255)
        if ball2.xcor() > 285:
            times += 0.5
            ball2.setx(285)
            ball2.dx *= -1.01
            pen1.clear()
            pen1.write(times,align='left',font=('Gang of Three',36,'normal'))
            playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
            r1 -= 2; g1 -= 1; b1 -= 5
            ball2.color(abs(r1%255),abs(g1%255),abs(b1%255))
        if ball2.xcor() < -285:
            times += 0.5
            ball2.setx(-285)
            ball2.dx *= -1.01
            pen1.clear()
            pen1.write(times,align='left',font=('Gang of Three',36,'normal'))
            playsound('D:\Programming\My programs\sounds\\bounce.wav',False)
            r1 -= 5; g1 -= 5; b1 -= 5
            ball2.color(abs(r1)%255,abs(g1)%255,abs(b1)%255)
    else:
        if ball2.ycor() > 260:
            ball2.sety(260)
            ball2.dy *= -1.01
        if ball2.ycor() < -260:
            ball2.sety(-260)
            ball2.dy *= -1.01
        if ball2.xcor() > 285:
            ball2.setx(285)
            ball2.dy *= -1.01
        if ball2.xcor() < -285:
            ball2.setx(-285)
            ball2.dy *= -1.01