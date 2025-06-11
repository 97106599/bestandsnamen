import os

mapje = input("welk mapje moet ik gebruiken?")
print(f"U heeft gekozen voor de map: {mapje}")
print(os.listdir(mapje))


def get_bestanden_in_map(map_pad):
    # Verkrijg de lijst met bestanden in de opgegeven map en submappen
    alle_bestanden = []

    for root, dirs, files in os.walk(map_pad):
        for bestand in files:
            # Voeg elke bestandsnaam toe aan de lijst
            volledige_pad = os.path.join(root, bestand)
            relatieve_pad = os.path.relpath(volledige_pad, start=map_pad)
            alle_bestanden.append(relatieve_pad)

    return alle_bestanden


def schrijf_bestanden_naar_tekstbestand(bestanden, uitvoer_pad):

    with open(uitvoer_pad, 'w', encoding='utf-8') as f:
        for bestand in bestanden:
            f.write(bestand + "\n")


def main():
    # Het pad naar de map 'bestandsnamen/movie_posters'
    map_pad = r"D:\Git\School\bestandsnamen\movie_posters"


    if not os.path.isdir(map_pad):
        print(f"De opgegeven map '{map_pad}' bestaat niet.")
        return


    bestanden = get_bestanden_in_map(map_pad)


    uitvoer_bestand = input("Voer de naam van het tekstbestand in (bijvoorbeeld 'bestandsnamen.txt'): ")


    uitvoer_pad = os.path.join(map_pad, uitvoer_bestand)


    schrijf_bestanden_naar_tekstbestand(bestanden, uitvoer_pad)

    print(f"De bestandsnamen zijn succesvol opgeslagen in: {uitvoer_pad}")


if __name__ == "__main__":
    main()

import os

def is_afbeelding(bestandsnaam):
    """Controleer of het bestand een afbeelding is op basis van de extensie."""
    extensies = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
    return bestandsnaam.lower().endswith(extensies)

def hernoem_alle_afbeeldingen(map_pad):
    """Hernoemt alle afbeeldingsbestanden in de map naar 'movie_poster_01.ext' formaat."""
    bestanden = []


    for root, dirs, files in os.walk(map_pad):
        for bestand in files:
            if is_afbeelding(bestand):
                volledig_pad = os.path.join(root, bestand)
                bestanden.append(volledig_pad)


    bestanden.sort()

    for index, oud_pad in enumerate(bestanden, 1):
        map_van_bestand = os.path.dirname(oud_pad)
        extensie = os.path.splitext(oud_pad)[1]
        nieuw_naam = f"movie_poster_{index:02d}{extensie}"
        nieuw_pad = os.path.join(map_van_bestand, nieuw_naam)

        print(f"Hernoemen: {oud_pad} → {nieuw_pad}")
        os.rename(oud_pad, nieuw_pad)


map_pad = r"D:\Git\School\bestandsnamen\movie_posters"

if os.path.isdir(map_pad):
    hernoem_alle_afbeeldingen(map_pad)
    print("Alle afbeeldingen zijn succesvol hernoemd.")
else:
    print(f"De map '{map_pad}' bestaat niet.")





