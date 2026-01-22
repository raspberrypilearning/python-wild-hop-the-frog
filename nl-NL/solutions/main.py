from p5 import *

x = 200 # horizontaal midden
y = 200 # verticaal midden
snelheid = 0
zwaartekracht = 1
springen = False

def mouse_pressed():
    global springen, snelheid
    if not springen:
        springen = True
        snelheid = -15

def setup():
    size(400, 400)
    no_stroke()
    global bg
    bg = load_image('background.png')

def draw():
    global y, snelheid, springen
    image(bg, 0, 0, width, height)

    rek = 30 if springen else 0

    fill('green')
    ellipse(x, y, 100, 80 + rek)                     # lichaam
    ellipse(x - 30, y + 30, 30, 20 + rek * 3)        # linkerpoot
    ellipse(x + 30, y + 30, 30, 20 + rek * 3)        # rechterpoot

    fill('white')
    circle(x - 20, y - 40 + rek / 2, 25)             # linkeroog
    circle(x + 20, y - 40 + rek / 2, 25)             # rechteroog

    fill('black')
    circle(x - 20, y - 40 + rek / 2, 10)             # linkerpupil
    circle(x + 20, y - 40 + rek / 2, 10)             # rechterpupil

    fill('red')
    ellipse(x, y + 20, 10, 30 - rek / 2)             # tong

    if springen:
        y += snelheid
        snelheid += zwaartekracht
        if y >= 200:
            y = 200
            snelheid = 0
            springen = False

run()
