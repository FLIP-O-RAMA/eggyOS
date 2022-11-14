def col():
 import main2

import os
import time

import turtle
from turtle import *

wn = turtle.Screen()   
wn.bgcolor('light blue')
wn.screensize(100000,100000)

go = 0
pen = "down"
turtles()
turtle.pendown()
while True:
  os.system("clear")
  go = input("(the pen is {}) up[u] down[d] left[l] right[r] pen[p] exit[ex]: ".format(pen))     
  if go == "u":
    turtle.forward(10)
    os.system("clear")
  elif go == "d":
    turtles()
    turtle.backward(10)
    os.system("clear")
  elif go == "l":
    turtles()
    turtle.left(25)
    os.system("clear")
  elif go == "r":
    turtles()
    turtle.right(25)
    os.system("clear")
  elif go == "p":
    os.system("clear")
    pen = input("pen_up[u] pen_down[d]: ")
    if pen == "u":
      pen = "up"
      turtles()
      turtle.penup()
      os.system("clear")
    elif pen == "d":
      pen = "down"
      turtles()
      turtle.pendown()
      os.system("clear")
  elif go == "ex":
    col()
    wn.bye()
    os.system("clear")