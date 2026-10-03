<h2 class="c-project-heading--task">Strek de poten van de kikker</h2>

\--- task ---

Laat de poten van de kikker zich strekken terwijl hij springt. 🐾

\--- /task ---

<h2 class="c-project-heading--explainer">Zet krachtig af!</h2>

Laten we nu de poten van de kikker strekken terwijl hij springt.  
We veranderen de **hoogte** van de poten met behulp van dezelfde `rek`-variabele.

Vermenigvuldig de 'rek' met een getal om de pootbeweging te overdrijven.  
Probeer `rek * 2` of `rek * 3`!

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 23
line_highlights: 31-32
---

def draw():
global y, snelheid, springen
image(bg, 0, 0, width, height)
fill('green')

    ```
    rek = 30 if springen else 0
    
    ellipse(x, y, 100, 80 + rek) # lichaam
    ellipse(x - 30, y + 30, 30, 20 + rek * 3) # linkerpoot
    ellipse(x + 30, y + 30, 30, 20 + rek * 3) # rechterpoot
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Een kikker midden in een sprong met gestrekte poten](images/step_7.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Als de benen te veel uitrekken, probeer dan te vermenigvuldigen met een kleiner getal. <br />
Strekken met `rek * 2` zal er zachter uitzien dan met `rek * 3`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als de poten er verkeerd uitzien:<br />

- Zorg ervoor dat je `rek * 3` optelt bij de **hoogte** van elke poot<br />
- Controleer nogmaals of de positie van de poten nog steeds `x - 30` en `x + 30` is

</div>