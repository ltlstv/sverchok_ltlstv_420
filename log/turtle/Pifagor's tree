from turtle import*
from math import* 
def fractal(aturt, depth, maxdepth):  
   if depth > maxdepth:  
     return 
   length = 180*((sqrt(2)/2)**depth)  
   anotherturt = aturt.clone()  
   aturt.forward(length)  
   aturt.left(45)  
   fractal(aturt, depth+1, maxdepth)  
   anotherturt.right(90)  
   anotherturt.forward(length)  
   anotherturt.left(90)  
   anotherturt.forward(length)  
   if depth != maxdepth:  
     turt3 = anotherturt.clone()  
     turt3.left(45)  
     turt3.forward(180*((sqrt(2)/2)**(1+depth)))  
     turt3.right(90)  
     fractal(turt3, depth+1, maxdepth)  
   anotherturt.left(90)  
   anotherturt.forward(length)  
 
def draw_fractal():  
   window = Screen()  
   t = Turtle()  
   t.hideturtle()  
   t.penup()  
   t.goto(-75, -225)  
   t.pendown()  
   t.speed(10)  
   t.left(90)  
   fractal(t, 1, 12)  
   window.exitonclick()  
 
draw_fractal()  
