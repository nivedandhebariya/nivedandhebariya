import turtle as t

t.penup()
t.goto(-20,230)
t.pendown()
t.left(45)

t.begin_fill()
t.fillcolor("#F1502F")
for j in range(4):
    for i in range(45):
        t.right(2)
        t.forward(1)
    t.forward(300)
t.end_fill()

t.penup()
t.goto(-70,180)
t.pendown()
t.pensize(20)
t.pencolor("white")
t.right(90)
t.forward(100)
t.pensize(50)
t.forward(1)
t.pensize(20)
t.forward(130)
t.pensize(50)
t.forward(1)
t.penup()
t.goto(0,100)
t.pendown()
t.right(45)
t.pensize(20)
t.forward(200)
t.pensize(50)
t.forward(1)
t.hideturtle()
t.done()