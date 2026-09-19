<h2 class="c-project-heading--task">Voeg een achtergrond toe</h2>

\--- task ---

Voeg een afbeelding toe die het hele scherm vult met een vijver op de achtergrond. 🐸🌿

\--- /task ---

<h2 class="c-project-heading--explainer">Het opzetten van de scene</h2>

Laten we beginnen met het toevoegen van een vijverachtergrond aan je scherm.  
Je gebruikt `load_image()` om een afbeelding te laden en `image()` om deze in elk frame te tekenen.

De afbeelding is al aanwezig en opgeslagen als **`background.png`** in dezelfde map als je code.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 12-13, 17
---

from p5 import \*

x = 200 # horizontaal midden
y = 200 # verticaal midden
snelheid = 0
zwaartekracht = 1
springen = False

def setup():
size(400, 400)
no_stroke()
global bg
bg = load_image('background.png')

def draw():
image(bg, 0, 0, width, height)

    ```
    # Teken Kikker hier
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![Een vijverachtergrond op volledig scherm](images/step_1.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Meer

De functie `image()` plaatst de afbeelding op een bepaalde positie.  <br />
Om het scherm te vullen, geef je `0, 0, width, height` door.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als de achtergrond niet verschijnt:<br />

- `global bg` moet in de `setup()`-functie staan.<br />
- Zorg ervoor dat 'background.png' tussen aanhalingstekens staat.<br />
- Gebruik `image(bg, 0, 0, width, height)` in `draw()`

</div>
