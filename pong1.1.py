# -*- coding: cp1252 -*-
# Juuso Nousiainen
# Pientä Python harjoittelua
# olio-pohjainen versio pelistä

import turtle

# määritellään oliot ja niiden attribuutit sekä funktiot

class Mela(turtle.Turtle):
    def __init__(self, x):
        #self.speed(0)
        super().__init__(shape = "square")
        self.color("white")
        self.shapesize(stretch_wid = 4, stretch_len = 0.8)
        self.penup()
        self.x = x
        self.goto(x, 0)

    def ylos(self):
        y = self.ycor()
        y += 40
        self.sety(y)
        if self.ycor() > 215: # jotta mela ei mene ulos kentältä
            self.sety(215)

    def alas(self):
        y = self.ycor()
        y -= 40
        self.sety(y)
        if self.ycor() < -215:
            self.sety(-215)


class Pallo(turtle.Turtle):
    
    def __init__(self, vasen, oikea, pisteet):
        super().__init__(shape = "square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 1
        self.dy = -1
        self.vasen = vasen
        self.oikea = oikea
        self.pisteet = pisteet
        self.piste1 = 0
        self.piste2 = 0

    def liiku(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        # jos osutaan kattoon tai lattiaan, muutetaan suunta
        if self.ycor() > 240:
            self.sety(240)
            self.dy *= -1

        if self.ycor() < -240:
            self.sety(-240)
            self.dy *= -1

        # pisteiden saaminen
        # siirretään pallo keskelle, muutetaan suunta
        # lisätään pelaajalle piste ja päivitetään tilanne
        if self.xcor() > 340:
            self.goto(0, 0)
            self.dx *= -1
            self.piste1 += 1
            self.pisteet.clear()
            self.pisteet.write("Pelaaja1 {} - {} Pelaaja2".format(self.piste1, \
                self.piste2), align="center", font=("Arial", 16, "normal"))

        if self.xcor() < -340:
            self.goto(0, 0)
            self.dx *= -1
            self.piste2 += 1
            self.pisteet.clear()
            self.pisteet.write("Pelaaja1 {} - {} Pelaaja2".format(self.piste1, \
                self.piste2), align="center", font=("Arial", 16, "normal"))

        # muutetaan suunta jos osutaan meloihin
        if (self.xcor() + 10 > 320) and (self.ycor() < self.oikea.ycor() + 50) \
           and (self.ycor() > self.oikea.ycor() - 50):
            self.dx *= -1

        if (self.xcor() - 10 < -320) and (self.ycor() < self.vasen.ycor() + 50)\
           and (self.ycor() > self.vasen.ycor() - 50):
            self.dx *= -1

    # päätetään peli
    def lopeta(self):
        self.pisteet.goto(0, 0)
        if (self.piste1 > self.piste2):
            self.pisteet.write("Peli päättyi. \nPelaaja1 voitti!", \
                            align = "center", font = ("Arial", 16, "normal"))
        else:
            self.pisteet.write("Peli päättyi. \nPelaaja2 voitti!", \
                            align = "center", font = ("Arial", 16, "normal"))


# pistetaulukko
class Pisteet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 210)
        self.write("Pelaaja1 0 - 0 Pelaaja2", align = "center", \
                   font = ("Arial", 16, "normal"))


def main():
    # luodaan pelikenttä turtlen avulla
    ikkuna = turtle.Screen()
    ikkuna.title("Pong")
    ikkuna.bgcolor("black")
    ikkuna.setup(700, 500)
    ikkuna.tracer(0)
    ikkuna.listen()
    
# luodaan oliot
    vasen = Mela(-330)
    oikea = Mela(330)
    pisteet = Pisteet()
    pallo = Pallo(vasen, oikea, pisteet)

# laitetaan ikkuna kuuntelemaan näppäimistöä 
    ikkuna.onkeypress(vasen.ylos, "a")
    ikkuna.onkeypress(vasen.alas, "z")
    ikkuna.onkeypress(oikea.ylos, "Up")
    ikkuna.onkeypress(oikea.alas, "Down")

# tehdään pelille silmukka
    while True:
        ikkuna.update()
        pallo.liiku()
        if pallo.piste1 == 15 or pallo.piste2 == 15:
            ikkuna.clear()
            ikkuna.bgcolor("black")
            pallo.lopeta()
            break
        

if __name__ == "__main__":
	main()

