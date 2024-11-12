"""
(CZ) OKO BERE - PRAVIDLA:
- Začínáš s 0 body.
- Počítač v každém kole vypíše, kolik máš bodů, a zeptá se tě, jestli chceš pokračovat.
- Pokud odpovíš „ne“, hra končí.
- Pokud odpovíš „ano“, počítač „otočí kartu“ (náhodně vybere číslo od 2 do 10), vypíše její hodnotu a přičte ji k bodům.
- Pokud máš víc než 21 bodů, prohráváš.
- Cílem hry je získat co nejvíc bodů, ideálně 21.

(EN) TWENTY-ONE GAME - RULES:
- You start with 0 points.
- In each round, the computer displays your current points and asks if you want to continue.
- If you answer “no”, the game ends.
- If you answer “yes”, the computer "draws a card" (randomly selects a number from 2 to 10), shows its value, and adds it to your points.
- If you have more than 21 points, you lose.
- The goal of the game is to get as close as possible to 21 points, ideally exactly 21.
"""

import random

total = 0
while total < 21:
    print('You have', total, 'points')
    answer = input('Draw a card? ')
    if answer == 'yes':
        card = random.randint(2, 11)
        print('You drew', card)
        total = total + card
    elif answer == 'no':
        break
    else:
        print('I don’t understand! Please answer "yes" or "no"')

if total == 21:
    print('Congratulations! You won!')
elif total > 21:
    print('Too bad!', total, 'points is too much!')
else:
    print('You were just', 21 - total, 'points away!')
