studenti = {"Anna": 12, "Petr": 13, "Eva": 11}

# Výpis všech studentů a jejich věku
for jmeno, vek in studenti.items():
    print(f"{jmeno} má {vek} let.")

print()

# Iterace přes klíče
for student in studenti:
    print(f"{student} má {studenti[student]} let.")