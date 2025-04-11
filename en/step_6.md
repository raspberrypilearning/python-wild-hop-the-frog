<h2 class="c-project-heading--task">Stretch the frog’s body</h2>
--- task ---
Make the frog’s body stretch when it jumps. 🎈
--- /task ---

<h2 class="c-project-heading--explainer">Add some bounce</h2>

Let’s add a bit of bounce to your frog! 🐸💥  
When the frog jumps, we can stretch its body to make the animation more dramatic.

We’ll use a variable called `stretch`.  
- When the frog is jumping, `stretch` is set to 30  
- When not jumping, `stretch` is 0  
- We add `stretch` to the **height** of the frog’s body shape

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 25, 27
---
def draw():
    global y, speed, jumping
    image(bg, 0, 0, width, height)
    fill('green')

    stretch = 30 if jumping else 0

    ellipse(x, y, 100, 80 + stretch)               # body
    ellipse(x - 30, y + 30, 30, 20)                # left foot
    ellipse(x + 30, y + 30, 30, 20)                # right foot

    fill('white')
    circle(x - 20, y - 40, 25)                     # left eye
    circle(x + 20, y - 40, 25)                     # right eye

    fill('black')
    circle(x - 20, y - 40, 10)                     # left pupil
    circle(x + 20, y - 40, 10)                     # right pupil

    fill('red')
    ellipse(x, y + 20, 10, 30)                     # tongue

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
![A frog with a stretched body mid-jump](images/step_6.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip 🌟

Try changing the stretch amount.  
Make your frog super tall by setting `stretch = 50` or just a little springy with `stretch = 10`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging 🧰

If the frog doesn’t stretch:<br />
- Make sure `stretch` is changing based on `jumping`<br />
- Check that it’s added to the **height** part of the ellipse

</div>