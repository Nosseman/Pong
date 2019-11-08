# -*- coding: cp1252 -*-
# Pientä Python harjoittelua
# Juuso Nousiainen

import turtle

# Luodaan peli-ikkuna
ikkuna = turtle.Screen()
ikkuna.title("Pong")
ikkuna.bgcolor("black")
ikkuna.setup(width=850, height=650)
ikkuna.tracer(0)

# Muuttujat pelaajien pisteille
pisteet1 = 0
pisteet2 = 0

# Luodaan melat
# Vasen:
melaV = turtle.Turtle()
melaV.speed(0)
melaV.shape("square")
melaV.color("white")
melaV.shapesize(stretch_wid=5, stretch_len=1)
melaV.penup()
melaV.goto(-400, 0)

# Oikea:
melaO = turtle.Turtle()
melaO.speed(0)
melaO.shape("square")
melaO.color("white")
melaO.shapesize(stretch_wid=5, stretch_len=1)
melaO.penup()
melaO.goto(400, 0)

# Luodaan pallo
pallo = turtle.Turtle()
pallo.speed(0)
pallo.shape("square")
pallo.color("white")
pallo.penup()
pallo.goto(0, 0)
pallo.dx = 1
pallo.dy = -1

# Luodaan scoreboard
pisteet = turtle.Turtle()
pisteet.speed(0)
pisteet.color("white")
pisteet.penup()
pisteet.hideturtle()
pisteet.goto(0, 270)
pisteet.write("Pelaaja1 0 - 0 Pelaaja2", align="center", font=("Arial", 20, "normal"))

# Funktiot melojen liikuttamiselle
def melaV_ylos():
    y = melaV.ycor()
    # määritellään paljonko mela liikkuu ylös
    y += 30
    # asetetaan uusi koordinaatti vanhan koordinaatin tilalle
    melaV.sety(y)
    # estetään melojen kentän ulkopuolelle meno
    if melaV.ycor() > 280:
        melaV.sety(280)

def melaV_alas():
    y = melaV.ycor()
    y -= 30
    melaV.sety(y)
    if melaV.ycor() < -280:
        melaV.sety(-280)

def melaO_ylos():
    y = melaO.ycor()
    y += 30
    melaO.sety(y)
    if melaO.ycor() > 280:
        melaO.sety(280)

def melaO_alas():
    y = melaO.ycor()
    y -= 30
    melaO.sety(y)
    if melaO.ycor() < -280:
        melaO.sety(-280)

# Asetetaan ikkuna kuuntelemaan näppäimistöä
ikkuna.listen()
ikkuna.onkeypress(melaV_ylos, "a")
ikkuna.onkeypress(melaV_alas, "z")
ikkuna.onkeypress(melaO_ylos, "Up")
ikkuna.onkeypress(melaO_alas, "Down")


# Silmukka pelille

while True:
    ikkuna.update()

    # Laitetaan pallo liikkumaan
    pallo.setx(pallo.xcor() + pallo.dx)
    pallo.sety(pallo.ycor() + pallo.dy)

    # Muutetaan pallon suunta sen osuessa ruudun ylä ja alalaitaan
    if pallo.ycor() > 315:
        pallo.sety(315)
        # vaihdetaan suunta
        pallo.dy *= -1

    if pallo.ycor() < -315:
        pallo.sety(-315)
        pallo.dy *= -1

    # Jos pallo ohittaa melan, siirretään takaisin keskelle
    if pallo.xcor() > 410:
        pallo.goto(0, 0)
        # vaihdetaan suunta
        pallo.dx *= -1
        # lisätään pelaaja1:lle piste
        pisteet1 += 1
        # tyhjennetään scoreboard teksti
        pisteet.clear()
        # korvataan scoreboard
        pisteet.write("Pelaaja1 {} - {} Pelaaja2".format(pisteet1, pisteet2), align="center", font=("Arial", 20, "normal"))

    if pallo.xcor() < -410:
        pallo.goto(0, 0)
        pallo.dx *= -1
        pisteet2 += 1
        pisteet.clear()
        pisteet.write("Pelaaja1 {} - {} Pelaaja2".format(pisteet1, pisteet2), align="center", font=("Arial", 20, "normal"))

    # Mitä tapahtuu jos pallot osuvat melaan
    if (pallo.xcor() > 390) and (pallo.ycor() < melaO.ycor() + 40) and (pallo.ycor() > melaO.ycor() - 40):
        pallo.dx *= -1

    if (pallo.xcor() < -390) and (pallo.ycor() < melaV.ycor() + 40) and (pallo.ycor() > melaV.ycor() - 40):
        pallo.dx *= -1
        
    # Päätetään peli kun toinen pelaajista saavuttaa pisterajan
    if (pisteet1 == 15) or (pisteet2 == 15):
        ikkuna.clear()
        ikkuna.bgcolor("black")
        pisteet.goto(0, 0)
        if (pisteet1 > pisteet2):
            pisteet.write("Peli päättyi. \nPelaaja1 voitti! ", align="center", font=("Arial", 20, "normal"))
        else:
            pisteet.write("Peli päättyi. \nPelaaja2 voitti! ", align="center", font=("Arial", 20, "normal"))
        break
    
