import os

from pymongo import MongoClient
from bson import ObjectId


def get_database():
    user = os.getenv("MONGO_USER", "root")
    password = os.getenv("MONGO_PASS", "example")
    host = os.getenv("MONGO_HOST", "mongo")
    port = os.getenv("MONGO_PORT", "27017")
    db_name = os.getenv("MONGO_DB", "Music-Library")

    uri = f"mongodb://{user}:{password}@{host}:{port}/?authSource=admin"
    client = MongoClient(uri)
    return client[db_name]


def get_collection(collection_name):
    db = get_database()
    return db[collection_name]


def insert_album(album):
    albums = get_collection('albums')
    result = albums.insert_one(album)
    return result.inserted_id


def get_all_albums():
    albums = get_collection("albums")
    result = []

    for doc in albums.find():
        doc["_id"] = str(doc["_id"])
        result.append(doc)

    return result


def remove_album_by_id(album_id):
    albums = get_collection("albums")
    result = albums.delete_one({"_id": ObjectId(album_id)})
    return result.deleted_count


def get_album(album_id):
    albums = get_collection("albums")
    result = albums.find_one({"_id": ObjectId(album_id)})
    return result


def find_album_by_name(name):
    albums = get_collection("albums")
    result = albums.find_one({"name": name})
    return result