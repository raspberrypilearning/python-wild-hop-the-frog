<h2 class="c-project-heading--task">Draw the frog's body and legs</h2>
--- task ---
Use green ellipses to draw the frog’s body and feet.
--- /task ---

<h2 class="c-project-heading--explainer">Draw your frog</h2>

Let’s draw a cartoon frog using a shape called an **ellipse**.  
An ellipse is like a squashed or stretched circle.

To draw one, use `ellipse(x, y, width, height)`  
- `x` and `y` control where it goes  
- `width` is how wide it is  
- `height` is how tall it is

We’ll use two variables, `x` and `y`, to control where the frog sits.  
The frog’s **body** is drawn at `(x, y)`, and the **feet** are drawn just below it using offsets like `x - 30` and `y + 30`.

This makes it easier to move the whole frog later by changing just `x` and `y`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights: 18-20
---
def draw():
    image(bg, 0, 0, width, height)
    fill('green')
    ellipse(x, y, 100, 80)               # body
    ellipse(x - 30, y + 30, 30, 20)      # left foot
    ellipse(x + 30, y + 30, 30, 20)      # right foot
--- /code ---
</div>

<div class="c-project-output">
![A green cartoon frog body and feet on a pond background](images/step_2.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Try changing the numbers to move the feet further apart or closer together.  
What happens if you draw them above the frog instead?

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If nothing shows up:<br />
- Make sure `fill()` comes *before* the `ellipse()` calls<br />
- Check that each `ellipse()` has four numbers inside<br />
- Make sure the `draw()` function is spelled correctly

</div>