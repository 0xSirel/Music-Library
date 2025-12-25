from musiclibrary.vinile import Vinile


class TestVinile:
    def test_creazione_vinile_completo(self):
        v = Vinile(
            "Artist",
            "Album",
            "2020",
            "IT",
            "http://url",
            ["LP"],
            ["Rock"],
            ["Punk"],
            ["123"],
        )
        assert v.artista == "Artist"
        assert v.formato == ["LP"]

    def test_creazione_vinile_valori_default(self):
        v = Vinile("Artist", "Album", "2020", "IT", "http://url")
        assert v.formato == []
        assert v.genere == []
        assert v.barcode == []

    def test_formato_singolo_diventa_lista(self):
        v = Vinile("Artist", "Album", "2020", "IT", "http://url", formato="LP")
        assert v.formato == ["LP"]

    def test_to_dict(self):
        v = Vinile("Artist", "Album", "2020", "IT", "http://url")
        d = v.to_dict()
        assert d["artista"] == "Artist"
        assert "formato" in d

    def test_descrizione(self):
        v = Vinile("Pink Floyd", "The Wall", "1979", "UK", "http://url")
        assert "Pink Floyd" in v.descrizione()
        assert "The Wall" in v.descrizione()

    def test_equality(self):
        v1 = Vinile("Artist", "Album", "2020", "IT", "http://url")
        v2 = Vinile("Artist", "Album", "2020", "IT", "http://url")
        assert v1 == v2

    def test_inequality(self):
        v1 = Vinile("Artist1", "Album", "2020", "IT", "http://url")
        v2 = Vinile("Artist2", "Album", "2020", "IT", "http://url")
        assert v1 != v2
