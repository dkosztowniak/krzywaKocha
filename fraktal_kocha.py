import turtle
import time

def krzywaKocha(d, n):
    f.pendown()
    if n == 0:
        f.forward(d)
    else:
        krzywaKocha(d/3, n-1)
        f.left(60)
        krzywaKocha(d/3, n-1)
        f.right(120)
        krzywaKocha(d/3, n-1)
        f.left(60)
        krzywaKocha(d/3, n-1)
    f.penup()

def platekKocha(d, n):
    for i in range(3):
        krzywaKocha(d, n)
        f.right(120)

kolory = ('#ffbd20', '#20bd20', '#ff3c00', '#f000ff', '#004aff')
xPlatek = (-400, -400, 200, 200, -100)
yPlatek = (-50, 250, 250, -50, 150)

f = turtle.Turtle()

turtle.title("Krzywa Kocha")

f.home()
f.penup()
f.pensize(2)
f.shape("classic")
f.speed(0) # 0..10 - najszybciej 0
f.clear()
f.hideturtle()

for n in range(5):
    # Legenda
    f.pencolor(kolory[n])
    f.goto(-450+(turtle.window_width()//5)*n, -380)
    f.write('n = ', True, align="left", font=("Arial", 12, "normal"))
    f.write(n, True, align="left", font=("Arial", 12, "normal"))

f.goto(-480, -350)
for n in range(5):
    f.pencolor(kolory[n])
    krzywaKocha(turtle.window_width()//5, n)

for n in range(5):
    f.pencolor(kolory[n])
    f.goto(xPlatek[n], yPlatek[n])
    platekKocha(200, n)