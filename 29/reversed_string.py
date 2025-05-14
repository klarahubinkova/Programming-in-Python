def obraceny_retezec(text):
    """
    Vrátí řetězec v opačném pořadí pomocí rekurze.

    Parametry:
    text (str): Vstupní text.

    Návratová hodnota:
    str: Obrácený řetězec.
    """
    if len(text) <= 1:
        return text
    return obraceny_retezec(text[1:]) + text[0]

print(obraceny_retezec("ahoj"))
