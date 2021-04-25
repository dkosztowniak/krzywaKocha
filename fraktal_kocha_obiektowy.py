import turtle

class fraktalKocha(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='classic', visible=False)

    def krzywaKocha(self, d, n):
        self.pendown()
        if n == 0:
            self.forward(d)
        else:
            self.krzywaKocha(d/3, n-1)
            self.left(60)
            self.krzywaKocha(d/3, n-1)
            self.right(120)
            self.krzywaKocha(d/3, n-1)
            self.left(60)
            self.krzywaKocha(d/3, n-1)
        self.penup()

    def platekKocha(self, d, n):
        for i in range(3):
            self.krzywaKocha(d, n)
            self.right(120)


kolory = ('#ffbd20', '#20bd20', '#ff3c00', '#f000ff', '#004aff')
xPlatek = (-400, -400, 200, 200, -100)
yPlatek = (-50, 250, 250, -50, 150)

f = fraktalKocha()

turtle.title('Krzywa Kocha')

f.home()
f.speed(0) # 0..10 - najszybciej 0
f.penup()
f.pensize(2)
f.clear()

for n in range(5):
    # Legenda
    f.pencolor(kolory[n])
    f.goto(-450+(turtle.window_width()//5)*n, -380)
    f.write('n = ', True, align="left", font=("Arial", 12, "normal"))
    f.write(n, True, align="left", font=("Arial", 12, "normal"))

f.goto(-480, -350)
for n in range(5):
    f.pencolor(kolory[n])
    f.krzywaKocha(turtle.window_width()//5, n)

for n in range(5):
    f.pencolor(kolory[n])
    f.goto(xPlatek[n], yPlatek[n])
    f.platekKocha(200, n)