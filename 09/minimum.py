# Zadání: Napiš program, který se pětkrát zeptá na číslo a nejmenší zadané číslo vypíše.
nejmensi = int(input("Zadej číslo: "))
for i in range(4):
    cislo = int(input("Zadej číslo: "))
    if cislo < nejmensi:
        nejmensi = cislo

print("Nejmenší ze zadaných čísel je", nejmensi)
