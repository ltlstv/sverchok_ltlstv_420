from turtle import*
lt(90)
def fr(w):
    if w>= 1:
        pensize(w)
        fd(w*10)
        rt(30)
        fr(w*0.75)
        lt(60)
        fr(w*0.75)
        rt(30)
        bk(w*10)
        pensize(w)
speed(10)
penup()
goto(0, -200 )
pendown()
hideturtle()
fr(10)
