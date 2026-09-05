<h2 class="c-project-heading--task">Laat de kikker terugvallen</h2>

\--- task ---

Gebruik de zwaartekracht om je kikker na de sprong weer op de grond te krijgen. 🪂

\--- /task ---

<h2 class="c-project-heading--explainer">Stijlvol vallen</h2>

Op dit moment springt je kikker omhoog en blijft hij springen. Laten we hem weer met beide poten op de grond zetten! 🌍  
We gebruiken de zwaartekracht om hem geleidelijk naar beneden te trekken en veilig te laten landen.

Zo werkt het:

- Zolang `springen` `True` is, voegen we `zwaartekracht` toe aan `snelheid`
- Hierdoor vertraagt de kikker, en valt vervolgens steeds sneller
- Wanneer de kikker de grond raakt, zetten we zijn positie terug en stoppen we de sprong

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
    if springen:
        y += snelheid
        snelheid += zwaartekracht
        if y >= 200:
            y = 200
            snelheid = 0
            springen = False
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Een kikker midden in een sprong die terugkeert naar de grond](images/step_5.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip 🌟

Probeer de waarde van `zwaartekracht` te wijzigen. <br />
Een hoger getal zorgt ervoor dat de kikker sneller valt. <br />
Een kleiner getal zorgt ervoor dat je kikker zachter landt! 🐸🌬️

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing 🧰

Als je kikker nooit landt:<br />

- Zorg ervoor dat `snelheid += zwaartekracht` zich binnen het `if springen:` blok bevindt<br />
- Controleer of `y >= 200` de landingsvoorwaarde is<br />
- Vergeet niet om `snelheid = 0` en `springen = False` weer in te stellen

</div>