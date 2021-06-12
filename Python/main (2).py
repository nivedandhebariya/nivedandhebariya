import turtle
import random  #Module for choosing random colors

spiral = turtle.Turtle()
colours = ["red", "blue", "black"]  #List of colors to use randomly

for i in range(40):
    spiral.color(random.choice(colours))  #Choosing the random colors from the colours list
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()