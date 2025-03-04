# Pevný vstup
text = "pes pes kočka pes kočka myš pes myš"

# Interaktivní vstup
#text = input("Zadej slova:")

# Rozdělení vstupu podle mezer
slova = text.split()

# Vytvoření prázdného slovníku
frekvence = {}

# Počítání výskytů slov
for slovo in slova:
    if slovo in frekvence:
        frekvence[slovo] += 1
    else:
        frekvence[slovo] = 1

print("Frekvence slov:", frekvence)