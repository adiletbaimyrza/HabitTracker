import os
from dotenv import load_dotenv
from flask import Flask
from routes import pages
from pymongo import MongoClient

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages)
    
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client["tracker"]
    
    return app