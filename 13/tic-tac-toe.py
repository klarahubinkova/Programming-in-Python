# Hra piškvorky pro dva hráče na poli 3x3
strana_pole = 3
hraci_pole = [" "] * (strana_pole * strana_pole)
konec_hry = False
hraci = ["o", "x"]
hrac_na_tahu = 0

while not konec_hry:
    if hrac_na_tahu == 0:
        hrac_na_tahu = 1
    else:
        hrac_na_tahu = 0

    for radek in range(0, strana_pole):
        for sloupec in range(0, strana_pole):
            index = strana_pole * radek + sloupec
            print(hraci_pole[index], end="")

            if sloupec < strana_pole - 1:
                print(" | ", end="")
            else:
                print()
        
        if radek < strana_pole - 1:
            print("- " * (2 * strana_pole - 1))
        else:
            print()
    
    print(f"Hráč '{hraci[hrac_na_tahu]}' na tahu.")
    
    vstup_radek = int(input("Zadej řádek: ")) - 1
    vstup_sloupec = int(input("Zadej sloupec: ")) - 1
    vstup_index = strana_pole * vstup_radek + vstup_sloupec

    while (not (0 <= vstup_radek and vstup_radek < strana_pole and 0 <= vstup_sloupec and vstup_sloupec < strana_pole)) or hraci_pole[vstup_index] != " ":
        if hraci_pole[vstup_index] != " ":
            print("Políčko je zabrané, vyber si jiné.")
        else:
            print("Takové políčko je mimo hrací plochu, zkus zadat jiné.")

        vstup_radek = int(input("Zadej řádek: ")) - 1
        vstup_sloupec = int(input("Zadej sloupec: ")) - 1
        vstup_index = strana_pole * vstup_radek + vstup_sloupec
    
    hraci_pole[vstup_index] = hraci[hrac_na_tahu]

    if (hraci_pole[0] == hraci_pole[1] and hraci_pole[1] == hraci_pole[2]) and hraci_pole[0] in hraci:
        print(f"Vyhrál hráč '{hraci_pole[0]}'")
        konec_hry = True
    elif (hraci_pole[3] == hraci_pole[4] and hraci_pole[4] == hraci_pole[5]) and hraci_pole[3] in hraci:
        print(f"Vyhrál hráč '{hraci_pole[3]}'")
        konec_hry = True
    elif (hraci_pole[6] == hraci_pole[7] and hraci_pole[7] == hraci_pole[8]) and hraci_pole[6] in hraci:
        print(f"Vyhrál hráč '{hraci_pole[6]}'")
        konec_hry = True
    elif (hraci_pole[0] == hraci_pole[3] and hraci_pole[3] == hraci_pole[6]) and hraci_pole[0] in hraci:
        print(f"Vyhrál hráč '{hraci_pole[0]}'")
        konec_hry = True
    elif (hraci_pole[1] == hraci_pole[4] and hraci_pole[4] == hraci_pole[7]) and hraci_pole[1] in hraci:
        print(f"Vyhrál hráč '{hraci_pole[1]}'")
        konec_hry = True
    elif (hraci_pole[2] == hraci_pole[5] and hraci_pole[5] == hraci_pole[8]) and hraci_pole[2] in hraci:
        print(f"Vyhrál hráč '{hraci_pole[2]}'")
        konec_hry = True
    elif (hraci_pole[0] == hraci_pole[4] and hraci_pole[4] == hraci_pole[8]) and hraci_pole[0] in hraci:
        print(f"Vyhrál hráč '{hraci_pole[0]}'")
        konec_hry = True
    elif (hraci_pole[2] == hraci_pole[4] and hraci_pole[4] == hraci_pole[6]) and hraci_pole[2] in hraci:
        print(f"Vyhrál hráč '{hraci_pole[2]}'")
        konec_hry = True
    
    if konec_hry:
        for radek in range(0, strana_pole):
            for sloupec in range(0, strana_pole):
                index = strana_pole * radek + sloupec
                print(hraci_pole[index], end="")

                if sloupec < strana_pole - 1:
                    print(" | ", end="")
                else:
                    print()
            
            if radek < strana_pole - 1:
                print("- " * (2 * strana_pole - 1))
            else:
                print()
