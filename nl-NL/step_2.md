<h2 class="c-project-heading--task">Teken de kikker</h2>

\--- task ---

Teken het lichaam en de poten van de kikker met behulp van ellipsen. 🐸🦵

\--- /task ---

<h2 class="c-project-heading--explainer">Teken het lichaam en de poten</h2>

Je kikker heeft een lijf en poten nodig!  
Je gebruikt `ellipse()` om ovalen te tekenen. 🥚

De functie `ellipse()` accepteert **4 argumenten**:

- x-positie
- y-positie
- breedte
- hoogte

Elk onderdeel van de kikker is **ten opzichte van de x- en y-as** geplaatst.  
Dit maakt het later makkelijker om te animeren.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 16
line_highlights: 20-23
---

def draw():
image(bg, 0, 0, width, height)

    ```
    # Teken hier de kikker
    fill('green')
    ellipse(x, y, 100, 80) # lichaam
    ellipse(x - 30, y + 30, 30, 20) # linkerpoot
    ellipse(x + 30, y + 30, 30, 20) # rechterpoot
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Een groen kikkerlichaam en -poten zittend op een waterlelieblad](images/step_2.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Probeer de getallen te veranderen om te zien hoe de vormen bewegen!  <br />
Let op hoe elk onderdeel **na** de achtergrond wordt getekend — anders zou het verborgen zijn.

</div>