# L. Louque
# 1/17/2023
# Emoji Starter Program  A+CR
#This program will draw an emoji face with eyes and a mouth

import turtle

#create the turtle object, set the speed and hide the turtle
t = turtle.Turtle()
t.speed(5)
t.hideturtle()

#set the position (x,y coordinate) of the turtle to begin drawing
#set the turtle facing right
t.setpos(0,-200)
t.setheading(0)
t.pensize(5)      #set the pensize-this can be changed
t.pendown()       #set the pen down to begin drawing


#draw the face (big circle)
def drawFace():
  t.fillcolor("yellow")
  t.pencolor("yellow")
  t.begin_fill()
  t.circle(200)
  t.end_fill()
  t.penup()
#draw left eye
def drawLeftEye():
  #draw sclera
  t.goto(-70,30)
  t.fillcolor("white")
  t.pencolor("white")
  t.pendown()
  t.begin_fill()
  t.circle(50)
  t.end_fill()
  t.penup()
  #draw pupil
  t.goto(-60,30)
  t.fillcolor("black")
  t.pencolor("black")
  t.pendown()
  t.begin_fill()
  t.circle(20)
  t.end_fill()
  t.penup()
#draw right eye
def drawRightEye():
  #draw sclera
  t.goto(70,30)
  t.fillcolor("white")
  t.pencolor("white")
  t.pendown()
  t.begin_fill()
  t.circle(50)
  t.end_fill()
  t.penup()
  #draw pupil
  t.goto(60,30)
  t.fillcolor("black")
  t.pencolor("black")
  t.pendown()
  t.begin_fill()
  t.circle(20)
  t.end_fill()
  t.penup()
#draw mouth
def drawMouth():
  t.goto(-100,-50)
  t.setheading(-60)
  t.fillcolor("white")
  t.pencolor("white")
  t.pendown()
  t.begin_fill()
  t.circle(120,140)
  t.end_fill()
  t.penup()

def drawEyes():
  drawLeftEye()
  drawRightEye()
drawFace()
drawEyes()
drawMouth()