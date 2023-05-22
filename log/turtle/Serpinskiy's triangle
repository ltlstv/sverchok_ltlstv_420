from turtle import*
 
def draw_sierpinski(length,depth):
    if depth==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        t.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)
 
window = Screen()
t = Turtle()
t.speed(10)
t.pensize(2)
t.penup()
t.goto(-200, -200)
t.pendown()
t.hideturtle()
draw_sierpinski(500,7)
window.exitonclick()
