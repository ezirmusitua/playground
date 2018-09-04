from config import Config
from services.database import Database
from models.user import _User

async def create_tables(app, loop):
  Database.connect(Config.db_uri)
  await Database.create_table(_User)

listeners = dict(
  before_server_start=[create_tables]
)
