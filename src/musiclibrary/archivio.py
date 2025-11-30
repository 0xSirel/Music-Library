import datetime
import json
import os
import shutil

from src.musiclibrary.vinile import Vinile


def salva_in_json(vinile):
    nome_file = "vinili.json"
    percorso_cartella = "Database"
    percorso_file = os.path.join(percorso_cartella, nome_file)

    os.makedirs(percorso_cartella, exist_ok=True)
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

    if not os.path.exists(percorso_file):
        with open(percorso_file, "w", encoding="utf-8") as file:
            json.dump([vinile_dict], file, indent=4, ensure_ascii=False)
    else:
        with open(percorso_file, encoding="utf-8") as file:
            try:
                archivio = json.load(file)
            except json.JSONDecodeError:
                archivio = []
        archivio.append(vinile_dict)
        with open(percorso_file, "w", encoding="utf-8") as file2:
            json.dump(archivio, file2, indent=4, ensure_ascii=False)


def stampa_archivio():
    percorso_cartella = "Database"
    percorso_file = os.path.join(percorso_cartella, "vinili.json")
    album_trovati = []
    if os.path.exists(percorso_file):
        with open(percorso_file, encoding="utf-8") as file:
            archivio = json.load(file)
            for vinile in archivio:
                vinile2 = Vinile(
                    vinile["artista"],
                    vinile["album"],
                    vinile["anno"],
                    vinile["paese"],
                    vinile["masterurl"],
                    vinile["formato"],
                    vinile["genere"],
                    vinile["style"],
                    vinile["barcode"],
                )
                album_trovati.append(vinile2)
    return album_trovati


def barcode_to_vinile(barcode):
    percorso_cartella = "Database"
    percorso_file = os.path.join(percorso_cartella, "vinili.json")
    if os.path.exists(percorso_file):
        with open(percorso_file, encoding="utf-8") as file:
            archivio = json.load(file)
            for vinile in archivio:
                barcodes = vinile["barcode"]
                if barcode in barcodes:
                    vinile2 = Vinile(
                        vinile["artista"],
                        vinile["album"],
                        vinile["anno"],
                        vinile["paese"],
                        vinile["masterurl"],
                        vinile["formato"],
                        vinile["genere"],
                        vinile["style"],
                        vinile["barcode"],
                    )
                    return vinile2
    return None


def rimuovi_vinile(vinile):
    percorso_cartella = "Database"
    percorso_file = os.path.join(percorso_cartella, "vinili.json")
    lista_vinili = []
    barcode_da_rimuovere = vinile.barcode

    with open(percorso_file, newline="", encoding="utf-8") as file:
        archivio = json.load(file)
        for vinile in archivio:
            if vinile["barcode"] != barcode_da_rimuovere:
                lista_vinili.append(vinile)

    with open(percorso_file, mode="w", newline="", encoding="utf-8") as file:
        json.dump(lista_vinili, file, indent=4, ensure_ascii=False)


def backup_database():
    percorso_cartella = "Database"
    percorso_cartella = os.path.join(percorso_cartella, "vinili.json")

    data_ora = datetime.datetime.now()
    nome_file = "backup-{}.json".format(data_ora.strftime("%Y-%m-%d_%H-%M-%S"))

    percorso_backup = "Backup"
    os.makedirs(percorso_backup, exist_ok=True)
    percorso_backup = os.path.join(percorso_backup, nome_file)

    shutil.copyfile(percorso_cartella, percorso_backup)


def stampa_backup():
    os.makedirs("Backup", exist_ok=True)
    percorso_cartella = "Backup"
    percorso_file = []
    for file in os.listdir(percorso_cartella):
        percorso_file.append(os.path.join(percorso_cartella, file))

    return percorso_file


def ripristina_backup(file):
    percorso_cartella = "Database"
    percorso_file = os.path.join(percorso_cartella, "vinili.json")
    shutil.copyfile(file, percorso_file)


def cancella_backup(file):
    os.remove(file)


def ricerca_artista(artista):
    percorso_cartella = "Database"
    percorso_cartella = os.path.join(percorso_cartella, "vinili.json")

    album_trovati = []
    with open(percorso_cartella, newline="", encoding="utf-8") as file:
        archivio = json.load(file)
        for vinile in archivio:
            if vinile["artista"] == artista:
                vinile2 = Vinile(
                    vinile["artista"],
                    vinile["album"],
                    vinile["anno"],
                    vinile["paese"],
                    vinile["masterurl"],
                    vinile["formato"],
                    vinile["genere"],
                    vinile["style"],
                    vinile["barcode"],
                )
                album_trovati.append(vinile2)
    return album_trovati


def ricerca_album(album):
    percorso_cartella = "Database"
    percorso_cartella = os.path.join(percorso_cartella, "vinili.json")

    album_trovati = []
    with open(percorso_cartella, newline="", encoding="utf-8") as file:
        archivio = json.load(file)
        for vinile in archivio:
            if vinile["album"] == album:
                vinile2 = Vinile(
                    vinile["artista"],
                    vinile["album"],
                    vinile["anno"],
                    vinile["paese"],
                    vinile["masterurl"],
                    vinile["formato"],
                    vinile["genere"],
                    vinile["style"],
                    vinile["barcode"],
                )
                album_trovati.append(vinile2)
    return album_trovati


def ricerca_anno(anno):
    percorso_cartella = "Database"
    percorso_cartella = os.path.join(percorso_cartella, "vinili.json")
    album_trovati = []

    with open(percorso_cartella, newline="", encoding="utf-8") as file:
        archivio = json.load(file)
        for vinile in archivio:
            if vinile["anno"] == anno:
                vinile2 = Vinile(
                    vinile["artista"],
                    vinile["album"],
                    vinile["anno"],
                    vinile["paese"],
                    vinile["masterurl"],
                    vinile["formato"],
                    vinile["genere"],
                    vinile["style"],
                    vinile["barcode"],
                )
                album_trovati.append(vinile2)
    return album_trovati


def ricerca_barcode(barcode):
    percorso_cartella = "Database"
    percorso_file = os.path.join(percorso_cartella, "vinili.json")

    with open(percorso_file, newline="", encoding="utf-8") as file:
        archivio = json.load(file)
        for vinile in archivio:
            if vinile["barcode"] == barcode:
                vinile2 = Vinile(
                    vinile["artista"],
                    vinile["album"],
                    vinile["anno"],
                    vinile["paese"],
                    vinile["masterurl"],
                    vinile["formato"],
                    vinile["genere"],
                    vinile["style"],
                    vinile["barcode"],
                )
                return vinile2
        return None


def in_archivio(barcode):
    percorso_cartella = "Database"
    percorso_file = os.path.join(percorso_cartella, "vinili.json")

    with open(percorso_file, newline="", encoding="utf-8") as file:
        archivio = json.load(file)
        for vinile in archivio:
            barcodes = vinile["barcode"]
            if barcode in barcodes:
                return True

    return False
