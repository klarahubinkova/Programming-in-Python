def faktorial(n):
    """
    Rekurzivně vypočítá faktoriál čísla n.

    Parametry:
    n (int): Číslo, jehož faktoriál chceme vypočítat (musí být nezáporné).

    Návratová hodnota:
    int: Faktoriál čísla n.
    """
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

cislo = 5
print(f"Faktoriál čísla {cislo} je {faktorial(cislo)}")
