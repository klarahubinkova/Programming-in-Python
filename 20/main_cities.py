# Uživatel hádá hlavní města, dokud neodpoví špatně nebo neuhodne všechna

# Slovník hlavních měst
hlavni_mesta = {
    "Česká republika": "Praha",
    "Slovensko": "Bratislava",
    "Německo": "Berlín",
    "Francie": "Paříž",
    "Itálie": "Řím"
}

# Převod do seznamu pro náhodný výběr
import random
zeme = list(hlavni_mesta.keys())
random.shuffle(zeme)  # Zamícháme pořadí zemí

# Hra
spravne = 0
for z in zeme:
    odpoved = input(f"Jaké je hlavní město {z}? ").strip()
    if odpoved.lower() == hlavni_mesta[z].lower():
        print("Správně!")
        spravne += 1
    else:
        print(f"Špatně, správná odpověď je {hlavni_mesta[z]}.")
        break

print(f"Hra skončila! Uhodl/a jsi {spravne} měst.")
