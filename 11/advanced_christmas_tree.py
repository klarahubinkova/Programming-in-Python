def vykresli_patro(sirka_stromu, vyska, min_sirka):
    '''
    Vykreslí patro stromu
    '''
    for i in range(vyska):
        print(" " * (sirka_stromu - min_sirka - i) + "*" * (2*(min_sirka + i) - 1))

def vykresli_kmen(sirka, vyska, sirka_stromu):
    '''
    Vykreslí kmen stromu
    '''
    for i in range(vyska):
        print(" " * (sirka_stromu - sirka//2 - 1) + "*" * (2*(sirka//2) + 1))

def vykresli_strom(pocet_pater, vyska_patra):
    '''
    Vykreslí celý strom
    '''
    velikost_stromu = pocet_pater * vyska_patra

    for cislo_patra in range(pocet_pater):
        vykresli_patro(velikost_stromu, vyska_patra, cislo_patra + 1)
    
    vykresli_kmen(velikost_stromu//10, velikost_stromu//5, velikost_stromu)

def nacti_input():
    '''
    Načte vstup od uživatele
    '''
    pocet_pater = int(input("Zadej počet pater stromu: "))
    vyska_patra = int(input("Zadej výšku patra: "))

    return pocet_pater, vyska_patra

pocet_pater, vyska_patra = nacti_input()
vykresli_strom(pocet_pater, vyska_patra)
