import aiosqlite
import attr

from config import Config

@attr.s
class Table(object):
  _cls = attr.ib(init=True)
  table_name = attr.ib(type=str, hash=True)
  fields = attr.ib(type=list, factory=list)
  foreign = attr.ib(type=dict, factory=dict)
  indexes = attr.ib(type=dict, factory=dict)

  def __attrs_post_init__(self):
    self.fields = Table.generate_fields_info(self._cls)

  @staticmethod
  def generate_fields_info(_cls):
    fields, foreign, indexes = list(), dict(), dict()
    for field in attr.fields(_cls):
      field_obj = dict(name=field.name)
      # type info
      if field.type == str:
        field_obj['type'] = 'TEXT'
      elif field.type == int:
        field_obj['type'] = 'INTEGER'
      elif field.type == float:
        field_obj['type'] = 'REAL'
      else:
        field_obj['type'] = 'BLOB'
      for key in field.metadata:
        if key.lower() in ['unique', 'notnull', 'primary', 'index',
                           'foreign']:
          field_obj[key] = field.metadata[key]
        if key.lower() == 'foreign':
          # foreign meta should set in format dict(foreign=(table, field_name))
          foreign[field['name']] = field.metadata['foreign']
        if key.lower() == 'index':
          # index meta should set in format dict(index='index_name')
          indexes[field['name']] = field.metadata['index']
      fields.append(field_obj)
    return fields, foreign, indexes

@attr.s
class TableWrapped(object):
  _database = attr.ib(type=aiosqlite.Connection)
  _table = attr.ib(type=Table)

  async def create_table(self):
    statement_check_exists = 'SELECT ' + self._table.table_name + \
                             ' FROM SQLITE_MASTER WHERE TYPE=\'TABLE\' ORDER ' \
                             'BY NAME;'
    cur = await self._database.execute(statement_check_exists)
    row = await cur.fetchone()
    await cur.close()
    print(row)
    statement_create = 'CREATE TABLE ' + self._table.table_name + '(\n'
    for field in self._table.fields:
      statement_create += field['name'] + ' ' + field['type'] + ' '
      if field['primary']:
        statement_create += 'PRIMARY KEY '
      if field['notnull']:
        statement_create += 'NOT NULL '
      if field['unique']:
        statement_create += 'UNIQUE'
      statement_create += ',\n'
    for field, params in self._table.foreign:
      statement_create += 'FOREIGN KEY (' + field + ') REFERENCES ' + \
                          params[0] + ' (' + params[1] + '),\n'
    statement_create = statement_create[:-2] + '\n);'
    print(statement_create)
    await self._database.execute(statement_create)
    for field, index_name in self._table.indexes:
      await self._database.execute(
        'CREATE UNIQUE INDEX ' + index_name + ' ON ' + self._table.table_name
        + '(' + field + ');'
      )
    await self._database.commit()

  async def find(self):
    pass

class Database(object):
  instance = None
  connection = None

  def __new__(cls, db_uri: str):
    if not Database.instance:
      Database.instance = object.__new__(cls)
      Database.instance.connection = aiosqlite.connect(db_uri)
    return Database.instance

  @staticmethod
  async def create_table(model):
    table = Table(model, model.table_name)
    table_wrapped = TableWrapped(Database.connection, table)
    # ensure table exists
    await table_wrapped.create_table()
