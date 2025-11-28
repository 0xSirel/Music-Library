from flask import Flask, jsonify, request

from src.musiclibrary.archivio import salva_in_json, stampa_archivio
from src.musiclibrary.gestoreAPI import cerca_per_album
from src.musiclibrary.vinile import Vinile

app = Flask(__name__)


@app.route("/api/search", methods=["GET"])
def cerca():
    nome = request.args.get("name")
    if not nome:
        return jsonify({"error": "Missing nome parameter"}), 400

    disponibili = cerca_per_album(nome)
    if not disponibili:
        return jsonify({"error": "No available albums found"}), 404

    disponibili_dict = [vinile.to_dict() for vinile in disponibili]

    return jsonify(disponibili_dict)


@app.route("/api/add", methods=["POST"])
def aggiungi():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    artista = data["artista"]
    album = data["album"]
    anno = data["anno"]
    country = data["country"]
    master_url = data["master_url"]
    formato = data["formato"]
    genere = data["genere"]
    style = data["style"]
    barcode = data["barcode"]

    vinile = Vinile(
        artista, album, anno, country, master_url, formato, genere, style, barcode
    )
    salva_in_json(vinile)
    return jsonify({"message": "Vinile added successfully"}), 201


@app.route("/api/print", methods=["GET"])
def stampa():
    disponibili = stampa_archivio()
    if not disponibili:
        return jsonify({"error": "No available albums found"}), 404
    disponibili_send = []
    for vinile in disponibili:
        disponibili_send.append(vinile.to_dict())

    return jsonify(disponibili_send)


@app.route("/api/health_check", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
