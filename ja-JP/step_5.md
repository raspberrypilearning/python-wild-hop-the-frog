<h2 class="c-project-heading--task">Make the frog fall back down</h2>

\--- task ---

Use gravity to bring your frog back to the ground after it jumps. 🪂

\--- /task ---

<h2 class="c-project-heading--explainer">Falling with style</h2>

Right now, your frog jumps up and keeps going. Let’s bring it back down to earth! 🌍  
We’ll use gravity to pull it down over time and land it safely.

Here’s how it works:

- While `jumping` is `True`, we add `gravity` to `speed`
- This makes the frog slow down, then fall faster and faster
- When the frog reaches the ground, we reset its position and stop the jump

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 44
line_highlights: 46-50
---

    ```
    if jumping:
        y += speed
        speed += gravity
        if y >= 200:
            y = 200
            speed = 0
            jumping = False
    ```

\--- /code ---

</div>

<div class="c-project-output">
![A frog mid-jump returning to land](images/step_5.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip 🌟

Try changing the `gravity` value. <br />
A higher number will make the frog fall faster. <br />
A smaller number will give your frog a gentler landing! 🐸🌬️

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging 🧰

If your frog never lands:<br />

- Make sure `speed += gravity` is inside the `if jumping:` block<br />
- Check for `y >= 200` as the landing condition<br />
- Don't forget to reset `speed = 0` and `jumping = False`

</div>