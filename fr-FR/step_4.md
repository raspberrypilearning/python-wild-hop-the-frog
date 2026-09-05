<h2 class="c-project-heading--task">Faire sauter la grenouille vers le haut</h2>

\--- task ---

Utilise une variable pour déplacer la grenouille vers le haut lorsque tu cliques avec la souris. 🖱️⬆️

\--- /task ---

<h2 class="c-project-heading--explainer">C'est l'heure de sauter !</h2>

Faisons bouger ta grenouille ! 🐸💨  
Tu la feras sauter vers le haut lorsque tu cliques sur la souris.

Utilise une variable appelée `sauter` pour suivre si la grenouille est en l'air.

- Quand tu cliques (n'importe où sur l'écran !), nous mettons `sauter = True`
- Si `sauter` est `True`, la grenouille se déplace vers le haut en utilisant une valeur `vitesse`

Pour faire sauter la grenouille, nous lui donnons une petite `vitesse` négative comme `-15`.  
Cela fait monter la position `y` — rappelle-toi, en code, plus petit `y` signifie plus haut sur l'écran !

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6
line_highlights: 9-13, 24, 44-45
---

gravité = 1
saut = False

def mouse_pressed():
global sauter, vitesse
if not sauter:
sauter = True
vitesse = -15

def setup():
size(400, 400)
no_stroke()
global bg
bg = load_image('background.png')

def draw():
global y, vitesse, sauter
image(bg, 0, 0, width, height)

    ```
    # Dessiner une grenouille ici
    fill('green')
    ellipse(x, y, 100, 80)               # corps
    ellipse(x - 30, y + 30, 30, 20)      # jambe gauche
    ellipse(x + 30, y + 30, 30, 20)      # jambe droite
    
    fill('white')
    circle(x - 20, y - 40, 25)           # oeil gauche
    circle(x + 20, y - 40, 25)           # oeil droit
    
    fill('black')
    circle(x - 20, y - 40, 10)           # pupille gauche
    circle(x + 20, y - 40, 10)           # pupille droite
    
    fill('red')
    ellipse(x, y + 20, 10, 30)           # langue
    
    if sauter:
        y += vitesse
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Une grenouille en plein saut après avoir cliqué](images/step_4.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce 🧠

Essaie de modifier la `vitesse` à `-10` ou `-20` et vois jusqu'où la grenouille saute. <br />
Nombres plus bas = sauts plus petits. Plus le nombre est élevé = plus le saut est important ! 🐸🚀

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer 🛠️

Si ta grenouille ne bouge pas :<br />

- Assure-toi que `mouse_pressed()` est correctement orthographié<br />
- Vérifie que `sauter = True` et `vitesse = -15` sont définis<br />
- Recherche `y += vitesse` à l'intérieur du bloc `if sauter:`

</div>