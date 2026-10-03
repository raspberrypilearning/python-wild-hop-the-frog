<h2 class="c-project-heading--task">Розтягни жабу</h2>

\--- task ---

Розтягни тіло своєї жабки, коли вона в повітрі. 🐸📏

\--- /task ---

<h2 class="c-project-heading--explainer">Стрибаємо вище</h2>

Коли жабка стрибає, вона тягне своє тіло, ніби дійсно відштовхується від землі.  
Ми можемо використати змінну, щоб зробити тіло довшим, поки жабка в повітрі.

Ми створимо змінну `stretch` і додамо її до висоти жабки, коли `jumping = True`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 23
line_highlights: 26, 30
---

def draw():
global y, speed, jumping
зображення(bg, 0, 0, ширина, height)
stretch = 30 if jumping else 0

    ```
    # Малюємо жабу тут
    fill('green')
    ellipse(x, y, 100, 80 + stretch)     # тіло
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Жабка з розтягнутим тілом у повітрі](images/step_6.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

Спробуй змінити `30` на `20` або `40`, щоб налаштувати розтягування. <br />
Можеш навіть змінювати значення під час стрибка, щоб зробити розтяг ще ефектнішим! 🎭

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо твоя жабка не розтягується:<br />

- Перевір, що `stretch = 30 if jumping else 0` стоїть перед `ellipse()`<br />
- Впевнись, що ти додаєш `stretch` до висоти тіла

</div>