<h2 class="c-project-heading--task">Rek de kikker uit</h2>

\--- task ---

Rek het lichaam van je kikker uit wanneer deze in de lucht is. 🐸📏

\--- /task ---

<h2 class="c-project-heading--explainer">Groter tijdens springen</h2>

Wanneer een kikker springt, strekt hij zijn lichaam uit zodat het lijkt alsof hij zich echt afzet tegen de grond.  
We kunnen een variabele gebruiken om het lichaam langer te maken terwijl de kikker in de lucht is.

We maken een variabele `rek` aan en tellen die op bij de hoogte van de kikker wanneer `springen = True`.

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
global y, snelheid, springen
image(bg, 0, 0, width, height)
rek = 30 if springen else 0

    ```
    # Teken hier een kikker
    fill('green')
    ellipse(x, y, 100, 80 + rek) # lichaam
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Een kikker met een uitgestrekt lichaam in de lucht](images/step_6.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Probeer de `30` te veranderen in `20` of `40` om de rek aan te passen. <br />
Je kunt de waarde zelfs tijdens het springen aanpassen om het effect dramatischer te maken! 🎭

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als je kikker zich niet uitrekt:<br />

- Controleer of `rek = 30 if springen else 0` vóór de `ellipse()` komt<br />
- Zorg ervoor dat je `rek` toevoegt aan de lichaamshoogte

</div>