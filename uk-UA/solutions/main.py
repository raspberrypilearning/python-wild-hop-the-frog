from p5 import *

x = 200 # горизонтальна середина
y = 200 # вертикальна середина
speed = 0
gravity = 1
jumping = False

def mouse_pressed():
    глобальні змінні: стрибок, швидкість
    якщо не стрибає:
        стрибок = Істина
        швидкість = -15

def setup():
    size(400, 400)
    no_stroke()
    глобальна змінна bg
    bg = load_image('background.png')

def draw():
    глобальні змінні: y, швидкість, стрибок
    image(bg, 0, 0, width, height)

    розтяг = 30 якщо стрибає, інакше 0

    fill('green')
    ellipse(x, y, 100, 80 + розтяг)                     # тіло
    ellipse(x - 30, y + 30, 30, 20 + розтяг * 3)        # ліва лапка
    ellipse(x + 30, y + 30, 30, 20 + розтяг * 3)        # права лапка

    fill('white')
    circle(x - 20, y - 40 + розтяг / 2, 25)             # ліве око
    circle(x + 20, y - 40 + розтяг / 2, 25)             # праве око

    fill('black')
    circle(x - 20, y - 40 + розтяг / 2, 10)             # лівий зіничка
    circle(x + 20, y - 40 + розтяг / 2, 10)             # правий зіничка

    fill('red')
    ellipse(x, y + 20, 10, 30 - розтяг / 2)             # язик

    якщо стрибає:
        y += швидкість
        швидкість += гравітація
        if y >= 200:
            y = 200
            speed = 0
            jumping = False

run()
