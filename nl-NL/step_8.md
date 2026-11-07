<h2 class="c-project-heading--task">Strek de ogen en de tong</h2>

\--- task ---

Laat de ogen van de kikker omhoog gaan en zijn tong inkrimpen wanneer hij springt! 👀👅

\--- /task ---

<h2 class="c-project-heading--explainer">Afwerking</h2>

Laten we de ogen uitrekken zodat ze omhoog gaan tijdens een sprong, en de tong inkrimpen zodat het lijkt alsof hij zich uit het waterlelieblad omhoog trekt.

Gebruik dezelfde `rek`-variabele om de `y`-posities en de hoogte te wijzigen.  
Dit geeft de animatie een extra professionele uitstraling! ✨

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 34
line_highlights: 35-36, 39-40, 43
---

    ```
    fill('white')
    circle(x - 20, y - 40 + rek / 2, 25) # linkeroog
    circle(x + 20, y - 40 + rek / 2, 25) # rechteroog
    
    fill('black')
    circle(x - 20, y - 40 + rek / 2, 10) # linkerpupil
    circle(x + 20, y - 40 + rek / 2, 10) # rechterpupil
    
    fill('red')
    ellipse(x, y + 20, 10, 30 - rek / 2) # tong
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Kikker met opgetrokken ogen en ingetrokken tong midden in een sprong](images/step_8.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Door een deel van de 'rek' toe te voegen aan of af te trekken van de oog- of tongpositie, worden deze geanimeerd. <br />
Kleinere rek = lagere ogen en langere tong. <br />
Grotere rek = hogere ogen en een kortere tong!

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als de ogen of de tong er vreemd uitzien:<br />

- Controleer de `+ rek / 2` of `- rek / 2` onderdelen nogmaals<br />
- Zorg ervoor dat je zowel de witte als de zwarte cirkels voor elk oog bijwerkt<br />

</div>

<div class="c-project-callout c-project-callout--tip">

### Terugkoppeling

Dit is een bètaproject, wat betekent dat het gloednieuw is en nog niet algemeen beschikbaar. Als je dit project zelf of met je club hebt getest, laat ons dan weten wat je ervan vindt.

<a href="https://form.raspberrypi.org/4874054?tfa_6933=python-wild-hop-the-frog" style="
display: inline-block;
padding: 10px 20px;
border: 2px solid black;
border-radius: 999px;
font-weight: bold;
font-size: 16px;
background-color: white;
color: black;
text-align: center;
text-decoration: none;
transition: background-color 0.2s;
" onmouseover="this.style.backgroundColor='#f0f0f0';" onmouseout="this.style.backgroundColor='white';">
Geef feedback </a>

</div>
