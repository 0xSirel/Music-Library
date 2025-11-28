from src.musiclibrary import gestoreAPI, archivio


def menu():
    while True:
        print("\n", "-" * 10, "Music Library", "-" * 10)
        print("1. Search album online")
        print("2. Print library")
        print("3. Search album in library")
        print("4. Search artist in library")
        print("5. Check album in library")
        print("6. Backup library")
        print("7. Restore backup")
        print("8. Delete backup")
        print("0. Exit")

        scelta = input("Choose an option: ")

        if scelta == "1":
            cerca_per_album_online()
        elif scelta == "2":
            stampa_libreria()
        elif scelta == "3":
            cerca_album_in_libreria()
        elif scelta == "4":
            cerca_artista_in_libreria()
        elif scelta == "5":
            gia_in_libreria()
        elif scelta == "6":
            backup_libreria()
        elif scelta == "7":
            ripristina_backup()
        elif scelta == "8":
            elimina_backup()
        elif scelta == "0":
            return


def elimina_backup():
    disponibili = archivio.stampa_backup()
    for idx, backup in enumerate(disponibili, 1):
        print(f"{idx}. {backup}")

    scelta = input("Choose an option: ")
    if 1 <= int(scelta) <= len(disponibili):
        backup_scelto = disponibili[int(scelta) - 1]
        archivio.cancella_backup(backup_scelto)
    else:
        print("Invalid choice")


def ripristina_backup():
    disponibili = archivio.stampa_backup()
    for idx, backup in enumerate(disponibili, 1):
        print(f"{idx}. {backup}")

    scelta = input("Choose an option: ")
    if 1 <= int(scelta) <= len(disponibili):
        backup_scelto = disponibili[int(scelta) - 1]
        archivio.ripristina_backup(backup_scelto)
    else:
        print("Invalid choice")


def gia_in_libreria():
    barcode = input("Insert barcode: ")
    result = archivio.in_archivio(barcode)
    if result:
        print(archivio.barcode_to_vinile(barcode), "Already in the library")
    else:
        print("Not in the library")


def backup_libreria():
    archivio.backup_database()


def cerca_artista_in_libreria():
    nome = input("Insert artist name: ")
    album_disponibili = archivio.ricerca_artista(nome)

    if album_disponibili:
        for idx, album in enumerate(album_disponibili, 1):
            print(f"{idx}. {album}")

            try:
                scelta = int(input("Choose an option or 0 to cancel: "))
                if scelta == 0:
                    print("Operation canceled")
                    return
                if scelta >= 1 or scelta <= len(album_disponibili):
                    album_scelto = album_disponibili[scelta - 1]

                    print(
                        f"\nSelected vinyl: {album_scelto.artista} - {album_scelto.album} ({album_scelto.anno})"
                    )
                    print(f"Country: {album_scelto.country}")
                    print(f"Master URL: {album_scelto.master_url}")
                    print(f"Formats: {', '.join(album_scelto.formato)}")
                    print(f"Barcode: {', '.join(album_scelto.barcode)}")
                    rimuovi = input(
                        "Do you want to remove it from the library? (y/n): "
                    )
                    if rimuovi == "y":
                        archivio.rimuovi_vinile(album_scelto)
                    else:
                        print("Not removed")
                else:
                    print("Invalid choice")

            except ValueError:
                print("Invalid choice")
    else:
        print("No album found")


def cerca_album_in_libreria():
    nome = input("Insert album name: ")
    album_disponibili = archivio.ricerca_album(nome)

    if album_disponibili:
        for idx, album in enumerate(album_disponibili, 1):
            print(f"{idx}. {album}")

            try:
                scelta = int(input("Choose an album or 0 to cancel: "))
                if scelta == 0:
                    print("Operation canceled")
                    return
                if scelta >= 1 or scelta <= len(album_disponibili):
                    album_scelto = album_disponibili[scelta - 1]

                    print(
                        f"\nSelected vinyl: {album_scelto.artista} - {album_scelto.album} ({album_scelto.anno})"
                    )
                    print(f"Country: {album_scelto.country}")
                    print(f"Master URL: {album_scelto.master_url}")
                    print(f"Formats: {', '.join(album_scelto.formato)}")
                    print(f"Barcode: {', '.join(album_scelto.barcode)}")
                    rimuovi = input(
                        "Do you want to remove it from the library? (y/n): "
                    )
                    if rimuovi == "y":
                        archivio.rimuovi_vinile(album_scelto)
                    else:
                        print("Not removed")
                else:
                    print("Invalid choice")

            except ValueError:
                print("Invalid choice")
    else:
        print("No album found")


def stampa_libreria():
    album_presenti = archivio.stampa_archivio()
    if not album_presenti:
        print("No vinyl found")
        return

    for album in album_presenti:
        print(album)


def cerca_per_album_online():
    nome = input("Insert album name: ")
    album_disponibili = gestoreAPI.cerca_per_album(nome)

    if album_disponibili:
        for idx, album in enumerate(album_disponibili, 1):
            print(f"{idx}. {album}")
    else:
        print("No album found")

    try:
        scelta = int(input("Choose an album or 0 to cancel: "))
        if scelta == 0:
            print("Operation canceled")
            return
        if scelta >= 1 or scelta <= len(album_disponibili):
            album_scelto = album_disponibili[scelta - 1]

            print(
                f"\nSelected vinyl: {album_scelto.artista} - {album_scelto.album} ({album_scelto.anno})"
            )
            print(f"Country: {album_scelto.country}")
            print(f"Master URL: {album_scelto.master_url}")
            print(f"Formats: {', '.join(album_scelto.formato)}")
            print(f"Barcode: {', '.join(album_scelto.barcode)}")
            aggiungi = input("Do you want to add it to the library? (y/n): ")
            if aggiungi == "y":
                if album_scelto.genere == [] or album_scelto.style == []:
                    gestoreAPI.estrai_da_master_url(album_scelto)
                archivio.salva_in_json(album_scelto)
            else:
                print("Not added")
        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid choice")
