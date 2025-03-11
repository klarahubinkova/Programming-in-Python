# Kámen, nůžky, papír

import random

# Možnosti hry
moznosti = ["kámen", "nůžky", "papír"]

# Slovník pravidel (co čím porážíme)
pravidla = {
    "kámen": "nůžky",  # kámen porazí nůžky
    "nůžky": "papír",  # nůžky porazí papír
    "papír": "kámen"   # papír porazí kámen
}

# Hra s while cyklem
while True:
    hrac = input("Zadej kámen, nůžky nebo papír (nebo 'konec' pro ukončení): ").strip().lower()
    
    if hrac == "konec":
        break

    if hrac not in moznosti:
        print("Neplatná volba, zkus to znovu.")
        continue

    pocitac = random.choice(moznosti)
    print(f"Počítač zvolil: {pocitac}")

    if hrac == pocitac:
        print("Remíza!")
    elif pravidla[hrac] == pocitac:
        print("Vyhrál/a jsi!")
    else:
        print("Prohrál/a jsi.")

print("Hra ukončena.")
