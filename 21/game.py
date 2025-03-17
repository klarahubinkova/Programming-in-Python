# Úkolem je vytvořit známou hru „Kdo? S kým? Co dělali?“
# Hra se hráče zeptá postupně na různé otázky, například „Kdo?“, „S kým?“, „Co dělali?“, „Kde?“, „Kdy?“, a nakonec „Proč?“, s tím, že mu umožní na jednu otázku odpovědět vícekrát a všechny odpovědi si uloží
# Na závěr pak hra z každé sady odpovědí vybere náhodně jednu odpověď a z takto vybraných odpovědí složí větu, kterou vypíše uživateli
# Seznam otázek by mělo být možné změnit v kódu na jednom místě bez zásahu do logiky programu

import random

# Definice otázek
otazky = ["Kdo?", "S kým?", "Co dělali?", "Kde?", "Kdy?", "Proč?"]

# Slovník pro uchování odpovědí
odpovedi = {
    "Kdo?": [],
    "S kým?": [],
    "Co dělali?": [],
    "Kde?": [],
    "Kdy?": [],
    "Proč?": []
}

# Sbírání odpovědí od uživatele
for otazka in otazky:
    print(f"{otazka} (napiš 'konec' pro ukončení zadávání odpovědí)")
    while True:
        odpoved = input("> ").strip()
        if odpoved.lower() == "konec":
            break
        odpovedi[otazka].append(odpoved)

# Výběr náhodných odpovědí
vybrane_odpovedi = []
for otazka in otazky:
    if len(odpovedi[otazka]) > 0:
        vybrane_odpovedi.append(random.choice(odpovedi[otazka]))

# Sestavení výsledné věty
vysledna_veta = " ".join(vybrane_odpovedi)

print("Vygenerovaná věta:")
print(vysledna_veta)
