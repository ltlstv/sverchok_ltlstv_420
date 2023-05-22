from turtle import*
 
def draw_partial_fern(t, size, angle, c1, c2):
    t.left(angle)
    draw_fern(t, size * c1)
    t.right(angle)
    t.backward(size * c2)
 
def draw_fern(t, size):
    if size > 1:
        t.forward(size)
        draw_partial_fern(t, size, 5, 0.8, 0.05)
        draw_partial_fern(t, size, -40, 0.45, 0.2)
        draw_partial_fern(t, size, 35, 0.4, 0.75)
 
def draw_art():
    window = Screen()
    fr = Turtle()
    fr.color("blue")
    fr.speed(0)
    fr.hideturtle()
    fr.left(90)
    draw_fern(fr, 60)
    window.exitonclick()
 
draw_art()
