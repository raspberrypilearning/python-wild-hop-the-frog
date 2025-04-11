<h2 class="c-project-heading--task">Move the eyes and stretch the tongue</h2>
--- task ---
Use the `stretch` variable to move the frog’s eyes and squash the tongue during a jump. 👀👅
--- /task ---

<h2 class="c-project-heading--explainer">Final touches</h2>

Let’s finish your frog with some fun details! 🐸✨  
In this step, the eyes **lift up** and the tongue gets **squashed** when the frog jumps.

We’re still using the same `stretch` variable:  
- The eyes move up slightly using `+ stretch / 2`  
- The tongue gets shorter using `30 - stretch / 2`

Small changes make your animation look more alive and bouncy!

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 25-27, 29-31
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
--- /code ---
</div>

<div class="c-project-output">
![A frog mid-jump with lifted eyes and a squashed tongue](images/step_8.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip 🎨

You can adjust the stretch effect to exaggerate the motion.  
Try making the tongue even shorter or the eyes move even higher!

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging 🔧

If nothing moves:<br />
- Check that the **eyes and tongue** use `+ stretch / 2` or `- stretch / 2`<br />
- Make sure `stretch` is changing while the frog is jumping

</div>