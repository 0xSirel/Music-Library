import pytest
from unittest.mock import patch
from musiclibrary import gestoreAPI
from musiclibrary.vinile import Vinile


def crea_vinile():
    return Vinile(
        artista="Neurotic Outsiders",
        album="Neurotic Outsiders",
        anno="1996",
        country="Europe",
        master_url="https://api.discogs.com/masters/410944",
        barcode=["1234567890"],
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


@patch("musiclibrary.gestoreAPI.requests.get")
def test_cerca_per_album_errore_api(mock_get):
    mock_get.return_value.status_code = 500
    with pytest.raises(RuntimeError, match="Error getting data"):
        gestoreAPI.cerca_per_album("test")


@patch("musiclibrary.gestoreAPI.requests.get")
def test_estrai_da_master_url_errore_api(mock_get):
    mock_get.return_value.status_code = 404
    vinile = crea_vinile()
    with pytest.raises(RuntimeError, match="Error getting data"):
        gestoreAPI.estrai_da_master_url(vinile)


@patch("musiclibrary.gestoreAPI.requests.get")
def test_cerca_per_album_senza_results(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"pagination": {}}
    risultati = gestoreAPI.cerca_per_album("albuminesistente")
    assert risultati == []
