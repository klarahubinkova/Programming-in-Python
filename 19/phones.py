# Telefonní seznam jako slovník
telefony = {
    "Máma": "777-123-456",
    "Táta": "608-987-654",
    "Babička": "602-333-222"
}

# Vyhledání čísla podle jména
jmeno = input("Zadej jméno pro vyhledání telefonu: ")

if jmeno in telefony:
    print(f"Telefonní číslo pro {jmeno} je {telefony[jmeno]}")
else:
    print("Osoba nebyla nalezena.")
