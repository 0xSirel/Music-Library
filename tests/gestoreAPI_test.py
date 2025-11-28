from musiclibrary import gestoreAPI
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

def test_cerca_per_album():
    vinile = crea_vinile()
    gestoreAPI.cerca_per_album(vinile)
    risultati = gestoreAPI.cerca_per_album("Neurotic Outsiders")
    assert len(risultati) > 0

def test_estrai_da_master_url():
    vinile = crea_vinile()
    vinile_obj = gestoreAPI.estrai_da_master_url(vinile)
    assert vinile_obj.artista == "Neurotic Outsiders"


if __name__ == "__main__":
    test_cerca_per_album()
    test_cerca_per_album()
    print("All tests passed")