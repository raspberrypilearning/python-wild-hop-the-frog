<h2 class="c-project-heading--task">Faire retomber la grenouille</h2>

--- task ---

Utilise la gravité pour ramener ta grenouille au sol après son saut. 🪂

--- /task ---

<h2 class="c-project-heading--explainer">Tomber avec style</h2>

Pour l'instant, ta grenouille saute et continue son chemin. Ramenons-la sur terre ! 🌍  
Nous utiliserons la gravité pour la faire descendre progressivement et la faire atterrir en toute sécurité.

Voici comment ça fonctionne :

- Tant que `sauter` est `True`, nous ajoutons `gravité` à `vitesse`
- Cela ralentit la grenouille, puis la fait tomber de plus en plus vite
- Lorsque la grenouille touche le sol, nous réinitialisons sa position et arrêtons le saut

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 44
line_highlights: 46-50
---

    if sauter:
        y += vitesse
        vitesse += gravité
        if y >= 200:
            y = 200
            vitesse = 0
            sauter = False

--- /code ---

</div>

<div class="c-project-output">
![Une grenouille en plein saut retombe sur la terre ferme](images/step_5.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce 🌟

Essaie de modifier la valeur de `gravité`. <br />
Un nombre plus élevé fera tomber la grenouille plus vite. <br />
Un nombre plus petit permettra à ta grenouille d'atterrir en douceur ! 🐸🌬️

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer 🧰

Si ta grenouille n'atterrit jamais :<br />

- Assure-toi que `vitesse += gravité` se trouve à l'intérieur du bloc `if sauter:`<br />
- Vérifie que `y >= 200` est la condition d'atterrissage<br />
- N'oublie pas de réinitialiser `vitesse = 0` et `sauter = False`

</div>