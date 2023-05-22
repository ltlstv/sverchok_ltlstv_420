from turtle import*
def koch(t, order, size):
    if order == 0:                 
        t.forward(size)
    else:
        koch(t, order-1, size/2.7)  
        t.left(60)
        koch(t, order-1, size/2.7)
        t.right(120)
        koch(t, order-1, size/2.7)
        t.left(60)
        koch(t, order-1, size/2.7)
 
fr = Turtle()
wn = Screen()
fr.speed(10)
fr.penup()
fr.backward(150)
fr.pendown()
fr.hideturtle()
fr.pensize(2)
fr.penup()
fr.goto(-400, -100)
fr.pendown()
 
koch(fr, 5, 500)
wn.exitonclick()
