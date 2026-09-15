<h2 class="c-project-heading--task">Ajouter un arrière-plan</h2>

\--- task ---

Ajoute une image qui remplit l'écran avec un étang en arrière-plan. 🐸🌿

\--- /task ---

<h2 class="c-project-heading--explainer">Planter le décor</h2>

Commençons par ajouter un étang en arrière-plan à ton écran.  
Tu utiliseras `load_image()` pour charger une image et `image()` pour la dessiner à chaque image.

L'image est déjà fournie et enregistrée sous le nom **`background.png`** dans le même dossier que ton code.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 12-13, 17
---

from p5 import \*

x = 200 # milieu horizontal
y = 200 # milieu vertical
vitesse = 0
gravité = 1
sauter = False

def setup():
size(400, 400)
no_stroke()
global bg
bg = load_image('background.png')

def draw():
image(bg, 0, 0, width, height)

    ```
    # Dessiner une grenouille ici
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![Un étang en arrière-plan en plein écran](images/step_1.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Plus

La fonction `image()` place l'image à une position.  <br />
Pour remplir l'écran, passe `0, 0, width, height`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si l'arrière-plan n'apparaît pas :<br />

- `global bg` doit figurer dans la fonction `setup()`.<br />
- Assure-toi que 'background.png' est entre guillemets.<br />
- Utilise `image(bg, 0, 0, width, height)` dans `draw()`

</div>
