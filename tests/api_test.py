import pytest
from unittest.mock import patch
from src.musiclibrary.main import app
from musiclibrary.vinile import Vinile


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestSearchAPI:
    def test_search_missing_param(self, client):
        response = client.get('/api/search')
        assert response.status_code == 400
        assert b"Missing" in response.data
    
    @patch('src.musiclibrary.main.cerca_per_album')
    def test_search_no_results(self, mock_cerca, client):
        mock_cerca.return_value = []
        response = client.get('/api/search?name=nonexistent')
        assert response.status_code == 404
    
    @patch('src.musiclibrary.main.cerca_per_album')
    def test_search_success(self, mock_cerca, client):
        mock_cerca.return_value = [Vinile("Artist", "Album", "2020", "IT", "http://url")]
        response = client.get('/api/search?name=test')
        assert response.status_code == 200


class TestAddAPI:
    def test_add_missing_json(self, client):
        response = client.post('/api/add')
        assert response.status_code == 415
    
    @patch('src.musiclibrary.main.database.insert_album')
    def test_add_success(self, mock_insert, client):
        mock_insert.return_value = "123abc"
        data = {
            "artista": "Test", "album": "Test", "anno": "2020",
            "country": "IT", "master_url": "http://url",
            "formato": [], "genere": [], "style": [], "barcode": []
        }
        response = client.post('/api/add', json=data)
        assert response.status_code == 201


class TestHealthCheck:
    def test_health_check(self, client):
        response = client.get('/api/health_check')
        assert response.status_code == 200
        assert b"ok" in response.data