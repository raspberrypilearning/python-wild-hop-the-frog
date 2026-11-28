<h2 class="c-project-heading--task">Dessiner la grenouille</h2>

\--- task ---

Utilise des ellipses pour dessiner le corps et les pattes de la grenouille. 🐸🦵

\--- /task ---

<h2 class="c-project-heading--explainer">Dessiner le corps et les jambes</h2>

Ta grenouille doit avoir un corps et de pattes !  
Tu utiliseras `ellipse()` pour dessiner des ovales. 🥚

La fonction `ellipse()` prend **4 arguments** :

- position x
- position y
- largeur
- hauteur

Chaque partie de la grenouille est placée **par rapport à `x` et `y`**.  
Cela facilitera l'animation plus tard.

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
    # Dessiner une grenouille ici
    fill('green')
    ellipse(x, y, 100, 80) # corps
    ellipse(x - 30, y + 30, 30, 20) # patte gauche
    ellipse(x + 30, y + 30, 30, 20) # patte droite
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Un corps et des pattes de grenouille verte assise sur un nénuphar](images/step_2.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Essaie de modifier les chiffres pour voir comment les formes bougent !  <br />
Remarque comment chaque partie est dessinée **après** l'arrière-plan — sinon elle serait cachée.

</div>