import turtle
t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()
s.tracer(20)
def square(color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.pendown()
        t.forward(10)
        t.right(90)
    t.end_fill()
    t.up()
    t.forward(10)
t.penup()
t.goto(-50,-100)
t.pendown()
for i in range(8):
    square("black")
