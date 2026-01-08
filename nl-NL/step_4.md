<h2 class="c-project-heading--task">Laat de kikker omhoog springen</h2>

\--- task ---

Gebruik een variabele om de kikker omhoog te bewegen wanneer je met de muis klikt. 🖱️⬆️

\--- /task ---

<h2 class="c-project-heading--explainer">Tijd om te springen!</h2>

Laten we je kikker in beweging krijgen! 🐸💨  
Je laat het omhoog springen als je met de muis klikt.

Gebruik een variabele genaamd `springen` om bij te houden of de kikker in de lucht is.

- Wanneer je klikt (ergens op het scherm!), stellen we `springen = True` in
- Als `springen` `True` is, beweegt de kikker omhoog met een `snelheid`-waarde

Om de kikker te laten springen, geven we hem een kleine negatieve snelheid, bijvoorbeeld -15.  
Hierdoor gaat de `y`-positie omhoog — onthoud dat in code een kleinere `y` hoger op het scherm betekent!

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6
line_highlights: 9-13, 24, 44-45
---

zwaartekracht = 1
springen = False

def mouse_pressed():
globale springen, snelheid
if not springen:
springen = True
snelheid = -15

def setup():
size(400, 400)
no_stroke()
global bg
bg = load_image('background.png')

def draw():
global y, snelheid, springen
image(bg, 0, 0, width, height)

    ```
    # Teken de kikker hier
    fill('green')
    ellipse(x, y, 100, 80) # lichaam
    ellipse(x - 30, y + 30, 30, 20) # linkerpoot
    ellipse(x + 30, y + 30, 30, 20) # rechterpoot
    
    fill('white')
    circle(x - 20, y - 40, 25) # linkeroog
    circle(x + 20, y - 40, 25) # rechteroog
    
    fill('black')
    cirkel(x - 20, y - 40, 10) # linkerpupil
    cirkel(x + 20, y - 40, 10) # rechter pupil
    
    vullen('red')
    ellips(x, y + 20, 10, 30) # tong
    
    if springen:
        y += snelheid
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Een kikker midden in een sprong na het klikken](images/step_4.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip 🧠

Probeer de `snelheid` eens te veranderen naar `-10` of `-20` en kijk hoe hoog de kikker springt. <br />
Lagere getallen = kleinere sprongen. Hogere getallen = grote sprongen! 🐸🚀

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing 🛠️

Als je kikker niet beweegt:<br />

- Zorg ervoor dat `mouse_pressed()` correct gespeld is<br />
- Controleer of `springen= True` en `snelheid = -15` zijn ingesteld<br />
- Zoek naar `y += snelheid` binnen het `if springen:` blok

</div>