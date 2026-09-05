from p5 import *

x = 200 # horizontal middle
y = 200 # vertical middle
speed = 0
gravity = 1
jumping = False

def mouse_pressed():
    global jumping, speed
    if not jumping:
        jumping = True
        speed = -15

def setup():
    size(400, 400)
    no_stroke()
    global bg
    bg = load_image('background.png')

def draw():
    global y, speed, jumping
    image(bg, 0, 0, width, height)

    stretch = 30 if jumping else 0

    fill('green')
    ellipse(x, y, 100, 80 + stretch)                     # body
    ellipse(x - 30, y + 30, 30, 20 + stretch * 3)        # left foot
    ellipse(x + 30, y + 30, 30, 20 + stretch * 3)        # right foot

    fill('white')
    circle(x - 20, y - 40 + stretch / 2, 25)             # left eye
    circle(x + 20, y - 40 + stretch / 2, 25)             # right eye

    fill('black')
    circle(x - 20, y - 40 + stretch / 2, 10)             # left pupil
    circle(x + 20, y - 40 + stretch / 2, 10)             # right pupil

    fill('red')
    ellipse(x, y + 20, 10, 30 - stretch / 2)             # tongue

    if jumping:
        y += speed
        speed += gravity
        if y >= 200:
            y = 200
            speed = 0
            jumping = False

run()
