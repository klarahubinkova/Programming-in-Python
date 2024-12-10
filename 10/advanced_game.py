# Zadání: Vytvoř hru, kde uživatel opakovaně hádá čísla mezi 1 a 10
import random

# Bez funkcí (je třeba dopředu znát počet opakování hry, uživatel si nemůže vybrat):
cislo = random.randint(1, 10)

print("Hádej číslo mezi 1 a 10.")
for pokus in range(3):
    tip = int(input("Tvůj tip: "))

    if tip == cislo:
        print("Správně!")
        break
    else:
        print("Špatně.")

print("Hádej číslo mezi 1 a 10.")
for pokus in range(3):
    tip = int(input("Tvůj tip: "))

    if tip == cislo:
        print("Správně!")
        break
    else:
        print("Špatně.")

print("Konec hry.")

print("*" * 30)

# S funkcemi:
def kolo_hry(pocet_pokusu):
    hadane_cislo = random.randint(1, 10)
    print("Hádej číslo mezi 1 a 10.")
    for pokus in range(pocet_pokusu):
        tip = int(input("Tvůj tip: "))

        if tip == hadane_cislo:
            print("Správně!")
            return
        else:
            print("Špatně.")

def hra():
    pocet_kol = int(input("Zadej počet kol: "))

    for kolo in range(pocet_kol):
        pocet_pokusu = int(input("Zadej počet pokusů: "))
        kolo_hry(pocet_pokusu)
    
    print("Konec hry.")

hra()
