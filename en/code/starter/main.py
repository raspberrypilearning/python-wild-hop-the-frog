from p5 import *

x = 200
y = 200
speed = 0
gravity = 1
jumping = False

def setup():
    size(400, 400)
    global bg
    bg = load_image('background.png')  # Load the background image
    no_stroke()


def draw():