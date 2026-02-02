<h2 class="c-project-heading--task">Dessiner les yeux et la langue</h2>

--- task ---

Ajoute des yeux blancs à pupilles noires et une langue rouge sous la grenouille.

--- /task ---

<h2 class="c-project-heading--explainer">Ajouter du caractère</h2>

Rendons ta grenouille plus expressive en lui ajoutant deux yeux blancs, des pupilles noires et une langue rouge. 👀👅

Utilise `circle(x, y, taille)` pour les yeux et les pupilles — les cercles sont simplement une version plus simple des ellipses.

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
    # Dessiner une grenouille ici

    fill('green')
    ellipse(x, y, 100, 80) # corps
    ellipse(x - 30, y + 30, 30, 20) # jambe gauche
    ellipse(x + 30, y + 30, 30, 20) # jambe droite
    
    fill('white')
    circle(x - 20, y - 40, 25) # œil gauche
    circle(x + 20, y - 40, 25) # œil droit
    
    fill('black')
    circle(x - 20, y - 40, 10) # pupille gauche
    circle(x + 20, y - 40, 10) # pupille droite
    
    fill('red')
    ellipse(x, y + 20, 10, 30) # langue


--- /code ---

</div>

<div class="c-project-output">
![Une grenouille de dessin animé avec des yeux blancs, des pupilles noires et une langue rouge](images/step_3.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Essaie de modifier la taille des yeux ou de la langue ! <br />  
Que se passe-t-il si tu rapproches ou éloignes les pupilles ?

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si tes yeux ou ta langue ne sont pas visibles :<br />

- Assure-toi que chaque forme possède le bon nombre de valeurs<br />
- Utilise `fill()` avant de dessiner chaque partie<br />
- Vérifie les fautes de frappe dans `circle()` et `ellipse()`

</div>