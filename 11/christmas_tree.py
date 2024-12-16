velikost = int(input("Zadej velikost: "))

# Koruna stromu
for i in range(velikost):
    print(" " * (velikost - i) + "*" * (2*i - 1))

# Kmen stromu
for i in range(velikost//4):
    print(" " * (velikost - 2) + "*" * 3)
