# Slovníkový cheatsheet: https://pyvec.github.io/cheatsheets/dicts/dicts-cs.pdf

# Vytvoření slovníku
studenti = {
    "Anna": 12,
    "Petr": 13,
    "Eva": 11
}

# Přístup k hodnotám
print(f"Anna má {studenti['Anna']} let.")

# Přidání nového studenta
studenti["Karel"] = 14
print(studenti)

# Změna hodnoty
studenti["Eva"] = 12

# Smazání studenta
del studenti["Petr"]

# Výpis celého slovníku
print(studenti)
