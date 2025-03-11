# Pro zadané číslo 'n' vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do 'n' a jako hodnoty k nim jejich druhé mocniny
# Příklad pro n = 4: {1: 1, 2: 4, 3: 9, 4: 16}

n = int(input("Zadej číslo: "))
mocniny = {}

for cislo in range(n + 1):
    mocniny[cislo] = cislo * cislo

print(mocniny)
