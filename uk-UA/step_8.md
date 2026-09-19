<h2 class="c-project-heading--task">Розтягни очі та язик жабки.</h2>

\--- task ---

Зроби так, щоб очі жабки піднімались, а язик зменшувався, коли вона підстрибує! 👀👅

\--- /task ---

<h2 class="c-project-heading--explainer">Останні штрихи</h2>

Давай розтягнемо очі, щоб вони піднімалися під час стрибка, і зменшимо язик, щоб виглядало так, ніби він підтягується з листочка латаття.

Використовуй ту ж саму змінну `stretch`, щоб змінити положення по `y` та висоту.  
Це додає анімації вишуканості! ✨

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
    circle(x - 20, y - 40 + stretch / 2, 25)   # ліве око
    circle(x + 20, y - 40 + stretch / 2, 25)   # праве око
    
    fill('black')
    circle(x - 20, y - 40 + stretch / 2, 10)   # лівий зіничка
    circle(x + 20, y - 40 + stretch / 2, 10)   # правий зіничка
    
    fill('red')
    ellipse(x, y + 20, 10, 30 - stretch / 2)   # язик
    ```

\--- /code ---

</div>

<div class="c-project-output">
![Жабка з піднятими очима та зменшеним язиком під час стрибка](images/step_8.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

Якщо додавати чи віднімати частину значення `stretch` від положення очей чи язика, вони будуть анімовані. <br />
Менше значення stretch = нижчі очі і довший язик. <br />
Більше значення stretch = вищі очі і коротший язик!

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо очі або язик виглядають дивно:<br />

- Перевір ще раз частини коду з `+ stretch / 2` чи `- stretch / 2`<br />
- Переконайся, що ти оновив і білі, і чорні кола для кожного ока<br />

</div>

<div class="c-project-callout c-project-callout--tip">

### Feedback

Це бета-версія проєкту, тобто він зовсім новий і ще не дуже популярний. Якщо ти вже тестував цей проєкт самостійно або з клубом, розкажи нам, що думаєш.

<a href=\"https://form.raspberrypi.org/4874054?tfa_6933=python-wild-hop-the-frog\\" style=\"
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
\" onmouseover=\"this.style.backgroundColor='#f0f0f0';\" onmouseout=\"this.style.backgroundColor='white';\">  Надіслати відгук </a>

</div>
