<h2 class="c-project-heading--task">Stretch the eyes and tongue</h2>
--- task ---
Make the frog’s eyes rise and its tongue shrink when it jumps! 👀👅
--- /task ---

<h2 class="c-project-heading--explainer">Finishing touches</h2>

Let’s stretch the eyes so they rise during a jump, and shrink the tongue to make it look like it’s pulling up from the lily pad.

Use the same `stretch` variable to change the `y` positions and height.  
This adds polish to the animation! ✨

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 34
line_highlights: 35-36, 39-40, 43
---
    fill('white')
    circle(x - 20, y - 40 + stretch / 2, 25)   # left eye
    circle(x + 20, y - 40 + stretch / 2, 25)   # right eye

    fill('black')
    circle(x - 20, y - 40 + stretch / 2, 10)   # left pupil
    circle(x + 20, y - 40 + stretch / 2, 10)   # right pupil

    fill('red')
    ellipse(x, y + 20, 10, 30 - stretch / 2)   # tongue
--- /code ---
</div>

<div class="c-project-output">
![Frog with rising eyes and shrinking tongue mid-jump](images/step_8.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Adding or subtracting part of `stretch` from the eye or tongue position will animate them. <br />
Smaller stretch = lower eyes and longer tongue. <br />
Bigger stretch = higher eyes and a shorter tongue!

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If the eyes or tongue look strange:<br />
- Double-check the `+ stretch / 2` or `- stretch / 2` parts<br />
- Make sure you update both the white and black circles for each eye<br />
- Try printing the `stretch` value to see what it’s doing

</div>