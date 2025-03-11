# Útěk z hradu

# Mapa hradu
mistnosti = {
    "chodba": {"východ": "kuchyně", "západ": "obývák"},
    "kuchyně": {"západ": "chodba"},
    "obývák": {"východ": "chodba", "jih": "tajná místnost"},
    "tajná místnost": {}  # Konec hry
}

aktualni_mistnost = "chodba"

# Herní smyčka
while True:
    print(f"Jsi v místnosti: {aktualni_mistnost}")
    moznosti = mistnosti[aktualni_mistnost]

    if not moznosti:
        print("Našel jsi tajnou místnost! Gratuluji, vyhrál jsi!")
        break

    print(f"Můžeš jít: {', '.join(moznosti.keys())}")
    smer = input("Kam chceš jít? ").strip().lower()

    if smer in moznosti:
        aktualni_mistnost = moznosti[smer]
    else:
        print("Tudy cesta nevede! Zkus to znovu.")
