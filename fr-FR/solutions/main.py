from p5 import *

x = 200 # milieu horizontal
y = 200 # milieu vertical
vitesse = 0
gravité = 1
sauter = False

def mouse_pressed():
    global saut, vitesse
    if not sauter:
        sauter = True
        vitesse = -15

def setup():
    size(400, 400)
    no_stroke()
    global bg
    bg = load_image('background.png')

def draw():
    global y, vitesse, sauter
    image(bg, 0, 0, width, height)

    etirement = 30 if sauter else 0

    fill('green')
    ellipse(x, y, 100, 80 + etirement) # corps
    ellipse(x - 30, y + 30, 30, 20 + etirement * 3) # pied gauche
    ellipse(x + 30, y + 30, 30, 20 + etirement * 3) # pied droit

    fill('white')
    circle(x - 20, y - 40 + etirement / 2, 25) # œil gauche
    circle(x + 20, y - 40 + etirement / 2, 25) # œil droit

    fill('black')
    circle(x - 20, y - 40 + etirement / 2, 10) # pupille gauche
    circle(x + 20, y - 40 + etirement / 2, 10) # pupille droite

    fill('red')
    ellipse(x, y + 20, 10, 30 - etirement / 2) # langue

    if sauter:
        y += vitesse
        vitesse += gravité
        if y >= 200:
            y = 200
            vitesse = 0
            sauter = False

run()
