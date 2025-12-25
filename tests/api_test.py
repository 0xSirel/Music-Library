import pytest
from unittest.mock import patch
from src.musiclibrary.main import app
from musiclibrary.vinile import Vinile


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestSearchAPI:
    def test_search_missing_param(self, client):
        response = client.get("/api/search")
        assert response.status_code == 400
        assert b"Missing" in response.data

    @patch("src.musiclibrary.main.cerca_per_album")
    def test_search_no_results(self, mock_cerca, client):
        mock_cerca.return_value = []
        response = client.get("/api/search?name=nonexistent")
        assert response.status_code == 404

    @patch("src.musiclibrary.main.cerca_per_album")
    def test_search_success(self, mock_cerca, client):
        mock_cerca.return_value = [
            Vinile("Artist", "Album", "2020", "IT", "http://url")
        ]
        response = client.get("/api/search?name=test")
        assert response.status_code == 200


class TestAddAPI:
    def test_add_missing_json(self, client):
        response = client.post("/api/add")
        assert response.status_code == 415

    @patch("src.musiclibrary.main.database.insert_album")
    def test_add_success(self, mock_insert, client):
        mock_insert.return_value = "123abc"
        data = {
            "artista": "Test",
            "album": "Test",
            "anno": "2020",
            "country": "IT",
            "master_url": "http://url",
            "formato": [],
            "genere": [],
            "style": [],
            "barcode": [],
        }
        response = client.post("/api/add", json=data)
        assert response.status_code == 201


class TestHealthCheck:
    def test_health_check(self, client):
        response = client.get("/api/health_check")
        assert response.status_code == 200
        assert b"ok" in response.data


class TestRemoveAPI:
    @patch("src.musiclibrary.main.database.remove_album_by_id")
    def test_remove_success(self, mock_remove, client):
        mock_remove.return_value = 1
        response = client.delete("/api/remove/507f1f77bcf86cd799439011")
        assert response.status_code == 200
        assert b"deleted_count" in response.data

    @patch("src.musiclibrary.main.database.remove_album_by_id")
    def test_remove_not_found(self, mock_remove, client):
        mock_remove.return_value = 0
        response = client.delete("/api/remove/507f1f77bcf86cd799439011")
        assert response.status_code == 404
        assert b"Album not found" in response.data


class TestGetByIdAPI:
    @patch("src.musiclibrary.main.database.get_album")
    def test_get_by_id_success(self, mock_get, client):
        from bson import ObjectId

        mock_get.return_value = {
            "_id": ObjectId("507f1f77bcf86cd799439011"),
            "artista": "Test Artist",
            "album": "Test Album",
            "anno": "2020",
            "country": "IT",
        }
        response = client.get("/api/get/507f1f77bcf86cd799439011")
        assert response.status_code == 200
        assert b"Test Artist" in response.data

    @patch("src.musiclibrary.main.database.get_album")
    def test_get_by_id_not_found(self, mock_get, client):
        mock_get.return_value = None
        response = client.get("/api/get/507f1f77bcf86cd799439011")
        assert response.status_code == 404
        assert b"Album not found" in response.data
