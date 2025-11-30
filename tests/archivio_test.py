import os
import json
from musiclibrary import archivio
from musiclibrary.vinile import Vinile


def crea_vinile():
    return Vinile(
        artista="Neurotic Outsiders",
        album="Neurotic Outsid3rs",
        anno="1996",
        country="Europe",
        master_url="https://api.discogs.com/masters/410944",
        barcode=["1234567890"]
    )


def crea_vinile_fake():
    return Vinile(
        artista="aaaaaaaaa",
        album="aaaaaaaa",
        anno="aaaaaaaa",
        country="aaaaaaaaaa",
        master_url="aaaaaaaaaa",
        barcode=["aaaaaaaa"]
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

    try:
        assert vinile_dict in file_json, "Album not saved in json"
    finally:
        archivio.rimuovi_vinile(vinile)


def test_in_archivio():
    vinile = crea_vinile()
    vinile_fake = crea_vinile_fake()

    archivio.salva_in_json(vinile)

    try:
        assert archivio.in_archivio("1234567890"), "Album not found in archive"
        assert not archivio.in_archivio(vinile_fake), "Album find in archive"
    finally:
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
    try:
        assert len(risultati) > 0
        assert any(v.artista == vinile.artista for v in risultati)

        risultati_falso = archivio.ricerca_artista("David Bowie")
        assert len(risultati_falso) == 0, "Album find in archive"
    finally:
        archivio.rimuovi_vinile(vinile)


def test_ricerca_album():
    vinile = crea_vinile()
    archivio.salva_in_json(vinile)
    risultati = archivio.ricerca_album("Neurotic Outsid3rs")
    try:
        assert len(risultati) > 0, "Album is not in archive"
        assert any(v.album == vinile.album for v in risultati)

        risultati_falso = archivio.ricerca_album("David Bowie")
        assert len(risultati_falso) == 0, "Album find in archive"
    finally:
        archivio.rimuovi_vinile(vinile)


def test_ricerca_anno():
    vinile = crea_vinile()
    archivio.salva_in_json(vinile)
    risultati = archivio.ricerca_anno("1996")
    try:
        assert len(risultati) > 0, "Album is not in archive"
        assert any(v.anno == vinile.anno for v in risultati), "Album don't match"

        risultati_falso = archivio.ricerca_anno("2000")
        assert len(risultati_falso) == 0, "Album find in archive"
    finally:
        archivio.rimuovi_vinile(vinile)


def test_ricerca_barcode():
    vinile = crea_vinile()
    archivio.salva_in_json(vinile)
    risultati = archivio.ricerca_barcode(vinile.barcode)
    try:
        assert risultati is not None, "Album is not in archive"
        assert risultati.barcode == vinile.barcode, "Album don't match"

        risultati_falso = archivio.ricerca_barcode("2000")
        assert risultati_falso is None, "Album find in archive"
    finally:
        archivio.rimuovi_vinile(vinile)


def test_stampa_archivio():
    vinile = crea_vinile()
    try:
        assert len(archivio.stampa_archivio()) == 0
        archivio.salva_in_json(vinile)
        assert len(archivio.stampa_archivio()) > 0
    finally:
        archivio.rimuovi_vinile(vinile)


def test_barcode_to_vinile():
    vinile = crea_vinile()
    archivio.salva_in_json(vinile)
    result_vinile = archivio.barcode_to_vinile(vinile.barcode[0])
    try:
        assert result_vinile is not None
        assert result_vinile.artista == vinile.artista
    finally:
        archivio.rimuovi_vinile(vinile)


def test_backup_database():

    vinile = crea_vinile()
    archivio.salva_in_json(vinile)
    assert len(archivio.stampa_backup()) == 0, "Archive is not empty"
    archivio.backup_database()
    disponibili = archivio.stampa_backup()
    try:
        assert len(disponibili) > 0
    finally:
        archivio.rimuovi_vinile(vinile)
        archivio.cancella_backup(disponibili[0])


def test_cancella_backup():
    vinile = crea_vinile()
    archivio.salva_in_json(vinile)
    archivio.backup_database()
    disponibili = archivio.stampa_backup()
    assert len(disponibili) > 0, "Archive is empty"
    archivio.cancella_backup(disponibili[0])

    try:
        disponibili = archivio.stampa_backup()
        assert len(disponibili) == 0, "Archive is not empty"
    finally:
        archivio.rimuovi_vinile(vinile)





