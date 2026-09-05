<h2 class="c-project-heading--task">Teken de ogen en de tong</h2>

\--- task ---

Voeg witte ogen met zwarte pupillen toe en een rode tong aan de onderkant van de kikker.

\--- /task ---

<h2 class="c-project-heading--explainer">Voeg wat karakter toe</h2>

Laten we je kikker wat expressiever maken door twee witte ogen, zwarte pupillen en een rode tong toe te voegen. 👀👅

Gebruik `circle(x, y, size)` voor de ogen en pupillen — cirkels zijn gewoon een vereenvoudigde versie van ellipsen.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 16
line_highlights: 25-27, 29-31, 33-34
---

def draw():
image(bg, 0, 0, width, height)
\# Teken hier de kikker

    ```
    fill('green')
    ellipse(x, y, 100, 80) # lichaam
    ellipse(x - 30, y + 30, 30, 20) # linkerpoot
    ellipse(x + 30, y + 30, 30, 20) # rechterpoot
    
    fill('white')
    circle(x - 20, y - 40, 25) # linkeroog
    circle(x + 20, y - 40, 25) # rechteroog
    
    fill('black')
    circle(x - 20, y - 40, 10) # linkerpupil
    cirkel(x + 20, y - 40, 10) # rechterpupil
    
    fill('red')
    ellips(x, y + 20, 10, 30) # tong
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Een cartoonkikker met witte ogen, zwarte pupillen en een rode tong](images/step_3.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Probeer de grootte van de ogen of de tong aan te passen! <br />  
Wat gebeurt er als je de pupillen dichter bij elkaar of verder uit elkaar beweegt?

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als je ogen of tong niet zichtbaar zijn:<br />

- Zorg ervoor dat elke vorm het juiste aantal waarden heeft<br />
- Gebruik `fill()` voordat je elk onderdeel tekent<br />
- Controleer op typfouten in `circle()` en `ellipse()`

</div>