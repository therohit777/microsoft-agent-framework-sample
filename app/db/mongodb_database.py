from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_mongo_connection():
    """
    Connect to MongoDB and return database and collection.
    
    Args:
        connection_string: MongoDB connection string
    
    Returns:
        tuple: (client, db, collection)
    """
    connection_string = os.getenv('MONGODB_URI')
    # connection_string = os.getenv('MONGODB_URI')
    client = MongoClient(connection_string)
    db = client.finance_db
    collection = db.message
    return collection