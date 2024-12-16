def vytiskni_okraj(sirka_prani, pocet_mezer):
    '''
    Vytiskne okraj
    '''
    sirka_pranicka = 1 + pocet_mezer + sirka_prani + pocet_mezer + 1
    print("*" * sirka_pranicka)

def vytiskni_odsazeni(sirka_prani, pocet_mezer):
    '''
    Vytiskne řádku mezi okrajem a přáním
    '''
    sirka_bez_okraje = pocet_mezer + sirka_prani + pocet_mezer
    print("*" + " " * sirka_bez_okraje + "*")

def vytiskni_prani(prani, pocet_mezer):
    '''
    Vytiskne řádku s přáním
    '''
    print("*" + " " * pocet_mezer + prani + " " * pocet_mezer + "*")

def vytiskni_pranicko(pocet_mezer = 2):
    '''
    Vytiskne přáníčko
    '''
    prani = input("Zadej přání (jinak bude nastaveno \"Merry X-MAS!\"): ")

    if len(prani) == 0:
        prani = "Merry X-MAS!"
    
    sirka_prani = len(prani)

    vytiskni_okraj(sirka_prani, pocet_mezer)
    vytiskni_odsazeni(sirka_prani, pocet_mezer)
    vytiskni_prani(prani, pocet_mezer)
    vytiskni_odsazeni(sirka_prani, pocet_mezer)
    vytiskni_okraj(sirka_prani, pocet_mezer)

vytiskni_pranicko()
