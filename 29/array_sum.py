def soucet(seznam):
    """
    Sečte všechny prvky v seznamu pomocí rekurze.

    Parametry:
    seznam (list of int): Seznam čísel.

    Návratová hodnota:
    int: Součet všech prvků.
    """
    if len(seznam) == 0:
        return 0
    
    if len(seznam) == 1:
        return seznam[0]
    
    return seznam[0] + soucet(seznam[1:])

print(soucet([1, 2, 3, 4]))
