from config import Config
from services.database import Database
from models.user import _User

async def create_tables(app, loop):
  print(Config)
  database = Database(Config().db_uri)
  await database.create_table(_User)

listeners = dict(
  before_server_start=[create_tables]
)
