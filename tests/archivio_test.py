import os
import json
from musiclibrary import archivio
from musiclibrary.vinile import Vinile

def crea_vinile():
    return Vinile(
        artista="Neurotic Outsiders",
        album="Neurotic Outsiders",
        anno="1996",
        country="Europe",
        master_url="https://api.discogs.com/masters/410944",
        barcode=["1234567890"]
    )

def test_salva_in_json():
    vinile = crea_vinile()

    archivio.salva_in_json(vinile)
    percorso_file = os.path.join("Database", "vinili.json")

    with open(percorso_file, "r", encoding="utf-8") as f:
        file_json = json.load(f)

    vinile_dict = {
        "artista": vinile.artista,
        "album": vinile.album,
        "anno": vinile.anno,
        "paese": vinile.country,
        "masterurl": vinile.master_url,
        "formato": vinile.formato,
        "genere": vinile.genere,
        "style": vinile.style,
        "barcode": vinile.barcode,
    }

    assert vinile_dict in file_json, "Album not saved in json"

    archivio.rimuovi_vinile(vinile)

def test_in_archivio():
    vinile = crea_vinile()

    archivio.salva_in_json(vinile)

    assert archivio.in_archivio("1234567890"), "Album not found in archive"

    vinile_fake = Vinile(
        artista="Fake Artist",
        album="Fake Album",
        anno="2025",
        country="Europe",
        master_url="http...",
        barcode=["0000000000"]
    )
    assert not archivio.in_archivio(vinile_fake), "Album find in archive"

    archivio.rimuovi_vinile(vinile)
    archivio.rimuovi_vinile(vinile_fake)

def test_rimuovi_vinile():
    vinile = crea_vinile()
    archivio.salva_in_json(vinile)
    archivio.rimuovi_vinile(vinile)
    assert not archivio.in_archivio(vinile), "Album find in archive"

def test_ricerca_artista():
    vinile = crea_vinile()
    archivio.salva_in_json(vinile)
    risultati = archivio.ricerca_artista("Neurotic Outsiders")
    assert len(risultati) > 0
    assert any(v.artista == vinile.album for v in risultati)

    risultati_falso = archivio.ricerca_artista("David Bowie")
    assert len(risultati_falso) == 0, "Album find in archive"

    archivio.rimuovi_vinile(vinile)


if __name__ == "__main__":
    test_salva_in_json()
    test_in_archivio()
    test_rimuovi_vinile()
    test_ricerca_artista()
    print("All tests passed")
