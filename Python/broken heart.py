import turtle

def my_goto(x, y):
    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(2)
t.width(12)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.color('red','blue')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()
t.pencolor('black')
t.penup()
t.goto(0,170)
t.pendown()
for zigzag in range(3):
    t.left(75)
    t.forward(40)
    t.right(65)
    t.forward(40)

my_goto(-150, -150)
turtle.write('BY :-_n.d._.05', font=("Bradley Hand ITC", 50, "bold")) 

turtle.hideturtle()
