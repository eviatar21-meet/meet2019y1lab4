import turtle

x=1
t=turtle.Turtle()
t.pensize(x)
def up():
   t.forward(5)
def down():
   t.forward(-5)
def left():
   t.left(5)
def right():
   t.right(5)
def pup():
   t.penup()
def pdown():
   t.pendown()


turtle.onkeypress(up, 'w')
turtle.onkeypress(down, 's')
turtle.onkeypress(left, 'a')
turtle.onkeypress(right, 'd')
turtle.onkeypress(pup, 'o')
turtle.onkeypress(pdown, 'l')  
turtle.listen()
turtle.mainloop()
