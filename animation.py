import turtle, math

turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(1)

def lerp(c1, c2, f):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * f) for i in range(3))

def filled_circle(cx, cy, r, edge_color, center_color, rings = 22):
    for i in range(rings):
        f = i / (rings - 1)
        rr = r * (1 - f)
        col = lerp(edge_color, center_color, f)
        t.penup()
        t.goto(cx, cy - rr)
        t.setheading(0)
        t.pendown()
        t.pencolor(col)
        t.circle(rr)

N =8
OR, OD = 185, 160
IR, ID = 150, 150

for k in range(N):
    a = math.radians(k * 360 / N)
    filled_circle(OD * math.cos(a), OD * math.sin(a), OR, (10, 15, 40), (70, 100, 170))

    for k in range(N):
        a = math.radians(k * 360 / N)
        filled_circle(ID * math.cos(a), ID * math.sin(a), IR, (30, 90, 130), (210, 245, 255))

turtle.done()