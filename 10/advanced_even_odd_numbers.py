# Zadání: Urči, zda jsou 3 čísla zadaná od uživatele sudá, nebo lichá

# Bez funkcí:
cislo = int(input("Zadejte číslo: "))

if cislo % 2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")

cislo = int(input("Zadejte číslo: "))

if cislo % 2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")

cislo = int(input("Zadejte číslo: "))

if cislo % 2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")

print("*" * 30)

# S funkcemi:
def sude_liche():
    cislo = int(input("Zadejte číslo: "))

    if cislo % 2 == 0:
        print("Číslo je sudé.")
    else:
        print("Číslo je liché.")

# Volání funkce
sude_liche()
sude_liche()
sude_liche()

print("*" * 30)

# Volání funkce s využitím for cyklu
for i in range(3):
    sude_liche()
