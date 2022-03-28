from pymongo import MongoClient
import os

cluster = MongoClient(os.getenv('URL_HOST'))

db = cluster[os.getenv('DB_NAME')]
