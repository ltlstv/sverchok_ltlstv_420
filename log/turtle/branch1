from turtle import*
from random import*
 
def drawFractalTree(t, depth, maxdepth):
    if depth > maxdepth:
        return
    else:
        for i in range(2):
            rand = randrange(-30, 30)
            t.left(rand)
            t.forward(50*(0.8)**depth)
            another = t.clone()
            drawFractalTree(another, depth+1, maxdepth)
        return
 
def draw_picture():
    window = Screen()
    tree = Turtle()
    tree.pensize(2)
    tree.penup()
    tree.goto(0, -200)
    tree.left(90)
    tree.pendown()
    tree.hideturtle()
    tree.speed(10)
    drawFractalTree(tree, 0, 12)
    window.exitonclick()
 
draw_picture()
