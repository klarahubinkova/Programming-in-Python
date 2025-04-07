def vytiskni_opakovane(text, pocet):
    """
    Vytiskne daný text několikrát podle parametru pocet.

    Parametry:
    text (str): Řetězec, který se má opakovaně vytisknout.
    pocet (int): Počet opakování textu.
    """
    for _ in range(pocet):
        print(text)

vytiskni_opakovane("Hello!", 3)
