from config import Config
from services.database import Database
from models import register_models

def prepare_database(app, loop):
  Database.connect(Config.db_uri)
  register_models(Database)
