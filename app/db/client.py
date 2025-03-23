from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection
import os

load_dotenv(verbose=True)


client = MongoClient(os.getenv("MONGODB_URL"))

db = client["nutrition"]
users_collection: Collection = db["users"]
