<h2 class="c-project-heading--task">Étirer les pattes de la grenouille</h2>

\--- task ---

Fais étirer les pattes de la grenouille lorsqu'elle saute. 🐾

\--- /task ---

<h2 class="c-project-heading--explainer">Propulser avec puissance !</h2>

Maintenant, étirons les pattes de la grenouille pendant qu'elle saute.  
Nous allons modifier la **hauteur** des pieds en utilisant la même variable `etirement`.

Multiplie l'« étirement » par un nombre pour exagérer le mouvement de la jambe.  
Essaie `etirement * 2` ou `etirement * 3` !

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
global y, vitesse, sauter
image(bg, 0, 0, width, height)
fill('green')

    ```
    etirement = 30 if sauter else 0
    
    ellipse(x, y, 100, 80 + etirement)                     # corps
    ellipse(x - 30, y + 30, 30, 20 + etirement * 3)        # jambe gauche
    ellipse(x + 30, y + 30, 30, 20 + etirement * 3)        # jambe droite
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Une grenouille en plein saut, les pattes tendues](images/step_7.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Si les jambes s'étirent trop, essaie de multiplier par un nombre plus petit. <br />
L'étirement par `etirement * 2` paraîtra plus doux que `etirement * 3`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si les pieds semblent incorrects :<br />

- Assure-toi d'ajouter `etirement * 3` à la **hauteur** de chaque pied<br />
- Vérifie que la position des jambes est toujours `x - 30` et `x + 30`

</div>