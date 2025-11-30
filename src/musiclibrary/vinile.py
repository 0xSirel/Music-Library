class Vinile:
    def __init__(
        self,
        artista,
        album,
        anno,
        country,
        master_url,
        formato=None,
        genres=None,
        style=None,
        barcode=None,
    ):
        if barcode is None:
            barcode = []
        if formato is None:
            formato = []
        if genres is None:
            genres = []
        if style is None:
            style = []

        self.artista = artista
        self.album = album
        self.anno = anno
        self.country = country
        self.master_url = master_url
        self.formato = (
            formato if isinstance(formato, list) else [formato] if formato else []
        )
        self.genere = genres if isinstance(genres, list) else [genres] if genres else []
        self.style = style if isinstance(style, list) else [style] if style else []
        self.barcode = (
            barcode if isinstance(barcode, list) else [barcode] if barcode else []
        )

    def descrizione(self):
        return (
            f"{self.artista} - {self.album} ({self.anno}) {self.country} {self.formato}"
        )

    def __str__(self):
        return self.descrizione()

    def to_dict(self):
        return {
            "artista": self.artista,
            "album": self.album,
            "anno": self.anno,
            "country": self.country,
            "master_url": self.master_url,
            "formato": self.formato,
            "genere": self.genere,
            "style": self.style,
            "barcode": self.barcode,
        }

    def __eq__(self, other):
        if not isinstance(other, Vinile):
            return NotImplemented
        return self.to_dict() == other.to_dict()
