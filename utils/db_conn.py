from os import getenv
from pymongo import MongoClient

URI = getenv("MONGODB_URI", "mongodb://localhost:27017/")
DB_NAME = getenv("VAULT_DB", "vault_logs")

_client = MongoClient(URI, serverSelectionTimeoutMS=500)

def get_collection(name: str = "notes"):
    """Return a MongoDB collection"""
    db = _client[DB_NAME]
    return db[name]
