# -*- coding: cp1252 -*-
# Pientä Python harjoittelua
# Juuso Nousiainen

import turtle

# Luodaan peli-ikkuna
ikkuna = turtle.Screen()
ikkuna.title("Pong")
ikkuna.bgcolor("black")
ikkuna.setup(width=800, height=600)
ikkuna.tracer(0)

# Luodaan melat
# Vasen:
melaV = turtle.Turtle()
melaV.speed(0)
melaV.shape("square")
melaV.color("white")
melaV.shapesize(stretch_wid=5, stretch_len=1)
melaV.penup()
melaV.goto(-350, 0)

# Oikea:
pallo = turtle.Turtle()
pallo.speed(0)
pallo.shape("square")
pallo.color("white")
pallo.penup()
pallo.goto(0, 0)
pallo.dx = 1
pallo.dy = -1

# Luodaan pallo
melaO = turtle.Turtle()
melaO.speed(0)
melaO.shape("square")
melaO.color("white")
melaO.shapesize(stretch_wid=5, stretch_len=1)
melaO.penup()
melaO.goto(350, 0)

# Funktiot melojen liikuttamiselle
def melaV_ylos():
    y = melaV.ycor()
    # määritellään paljonko mela liikkuu ylös
    y += 20
    # asetetaan uusi koordinaatti vanhan koordinaatin tilalle
    melaV.sety(y)
    # estetään melojen kentän ylimeno
    if melaV.ycor() > 250:
        melaV.sety(250)

def melaV_alas():
    y = melaV.ycor()
    y -= 20
    melaV.sety(y)
    if melaV.ycor() < -250:
        melaV.sety(-250)

def melaO_ylos():
    y = melaO.ycor()
    y += 20
    melaO.sety(y)
    if melaO.ycor() > 250:
        melaO.sety(250)

def melaO_alas():
    y = melaO.ycor()
    y -= 20
    melaO.sety(y)
    if melaO.ycor() < -250:
        melaO.sety(-250)

# Asetetaan ikkuna kuuntelemaan näppäimistöä
ikkuna.listen()
ikkuna.onkeypress(melaV_ylos, "a")
ikkuna.onkeypress(melaV_alas, "z")
ikkuna.onkeypress(melaO_ylos, "Up")
ikkuna.onkeypress(melaO_alas, "Down")


# Silmukka
while True:
    ikkuna.update()

    # Laitetaan pallo liikkumaan
    pallo.setx(pallo.xcor() + pallo.dx)
    pallo.sety(pallo.ycor() + pallo.dy)

    # Muutetaan pallon suunta sen osuessa ruudun ylä ja alalaitaan
    if pallo.ycor() > 290:
        pallo.sety(290)
        # vaihdetaan suunta
        pallo.dy *= -1

    if pallo.ycor() < -290:
        pallo.sety(-290)
        pallo.dy *= -1

    # Jos pallo ohittaa melan, siirretään takaisin keskelle
    if pallo.xcor() > 390:
        pallo.goto(0, 0)
        # vaihdetaan suunta
        pallo.dx *= -1

    if pallo.xcor() < -390:
        pallo.goto(0, 0)
        pallo.dx *= -1

    # Mitä tapahtuu jos pallot osuvat melaan

    if pallo.xcor() > 340 and pallo.ycor() < melaO.ycor() + 40 and pallo.ycor() > melaO.ycor() -40:
        pallo.dx *= -1

    if pallo.xcor() < -340 and pallo.ycor() < melaV.ycor() + 40 and pallo.ycor() > melaV.ycor() -40:
        pallo.dx *= -1
