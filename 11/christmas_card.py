prani = input("Zadej přání (jinak bude nastaveno \"Merry X-MAS!\"): ")

if len(prani) == 0:
    prani = "Merry X-MAS!"

pocet_mezer = 2
sirka_bez_okraje = pocet_mezer + len(prani) + pocet_mezer
sirka_prani = 1 + sirka_bez_okraje + 1

print("*" * sirka_prani)
print("*" + " " * sirka_bez_okraje + "*")
print("*" + " " * pocet_mezer + prani + " " * pocet_mezer + "*")
print("*" + " " * sirka_bez_okraje + "*")
print("*" * sirka_prani)
