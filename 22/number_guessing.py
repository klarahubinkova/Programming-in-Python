import random

nahodne_cislo = random.randint(1, 20)
odpoved = int(input("Zadej svůj tip: "))

while not (odpoved == nahodne_cislo):
    if odpoved < nahodne_cislo:
        print("Zkus větší!")
    else:
        print("Zkus menší!")

    odpoved = int(input("Zadej svůj tip: "))

print("Tvůj tip byl správný")
