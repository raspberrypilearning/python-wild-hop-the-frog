<h2 class="c-project-heading--task">Stretch the frog’s legs</h2>
--- task ---
Use the same `stretch` value to make the frog’s legs grow when it jumps. 🦵🦵
--- /task ---

<h2 class="c-project-heading--explainer">Add extra spring</h2>

Your frog’s body stretches when it jumps — now let’s do the same for its legs.  
This will make the whole frog feel more bouncy and alive! 🐸💨

We’ll use the same `stretch` variable and add it to the **height** of the feet.  
You can make the effect bigger by multiplying `stretch`, like this: `stretch * 3`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 26-27
---
def draw():
    global y, speed, jumping
    image(bg, 0, 0, width, height)
    fill('green')

    stretch = 30 if jumping else 0

    ellipse(x, y, 100, 80 + stretch)                     # body
    ellipse(x - 30, y + 30, 30, 20 + stretch * 3)        # left foot
    ellipse(x + 30, y + 30, 30, 20 + stretch * 3)        # right foot

    fill('white')
    circle(x - 20, y - 40, 25)                           # left eye
    circle(x + 20, y - 40, 25)                           # right eye

    fill('black')
    circle(x - 20, y - 40, 10)                           # left pupil
    circle(x + 20, y - 40, 10)                           # right pupil

    fill('red')
    ellipse(x, y + 20, 10, 30)                           # tongue

    if jumping:
        y += speed
        speed += gravity
        if y >= 200:
            y = 200
            speed = 0
            jumping = False
--- /code ---
</div>

<div class="c-project-output">
![Frog with springy stretched legs mid-jump](images/step_7.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip 💡

Try changing the multiplier on the legs.  
What happens if you use `stretch * 2` or `stretch * 5` instead?

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging 🧩

If your frog’s legs don’t stretch:<br />
- Make sure you added `stretch * 3` to the **height** of the ellipses<br />
- Check that both feet are updated the same way

</div>