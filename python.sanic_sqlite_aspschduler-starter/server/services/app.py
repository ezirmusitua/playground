from sanic import Sanic
from sanic.response import json
import aiosqlite

import os

DB_PATH = os.path.join(
  os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data/test.db')

app = Sanic()

@app.listener('before_server_start')
async def init_db(app, loop):
  print('creating db', DB_PATH)
  async with aiosqlite.connect(DB_PATH) as db:
    await db.execute('''
    CREATE TABLE test_table (
      column1 INTEGER PRIMARY KEY,
      column2 INTEGER,
      column3 INTEGER 
    );
    ''')
    await db.commit()
  # async with db.execute('SELECT * FROM some_table') as cursor:
  #   async for row in cursor:
  #     print(row)

@app.route('/')
async def test(request):
  return json({'hello': 'world'})

@app.route('/block')
async def test_blocked(request):
  return json({'hello': 'blocked world'})

if __name__ == '__main__':
  app.run(port=8000, debug=True)
