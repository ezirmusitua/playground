from sqlite3 import OperationalError

import aiosqlite
import attr

@attr.s
class Table(object):
  _cls = attr.ib(init=True)
  table_name = attr.ib(type=str, hash=True)
  fields = attr.ib(type=list, factory=list)
  foreign = attr.ib(type=dict, factory=dict)
  indexes = attr.ib(type=dict, factory=dict)

  def __attrs_post_init__(self):
    self.fields, self.foreign, self.indexes = Table.generate_fields_info(
      self._cls)

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
  _current_statement = attr.ib(type=str, default='')

  async def is_table_exists(self):
    statement_check_exists = 'SELECT ' + self._table.table_name + \
                             ' FROM SQLITE_MASTER WHERE TYPE=\'TABLE\' ORDER ' \
                             'BY NAME;'
    async with self._database:
      try:
        print(statement_check_exists)
        cur = await (self._database.execute(statement_check_exists))
        print('cur', cur)
        row = await cur.fetchone()
        print(row)
        await cur.close()
        return False
      except OperationalError as e:
        return True

  async def create_table(self):
    if self.is_table_exists(): return
    async with self._database:
      statement_create = 'CREATE TABLE ' + self._table.table_name + '(\n'
      for field in self._table.fields:
        statement_create += (field['name'] + ' ' + field['type'] + ' ')
        if field.get('primary'):
          statement_create += 'PRIMARY KEY '
        if field.get('notnull'):
          statement_create += 'NOT NULL '
        if field.get('unique'):
          statement_create += 'UNIQUE'
        statement_create += ',\n'
      for field, params in self._table.foreign:
        statement_create += 'FOREIGN KEY (' + field + ') REFERENCES ' + \
                            params[0] + ' (' + params[1] + '),\n'
      statement_create = statement_create[:-2] + '\n);'
      await self._database.execute(statement_create)
      for field, index_name in self._table.indexes:
        await self._database.execute(
          'CREATE UNIQUE INDEX ' + index_name + ' ON ' +
          self._table.table_name
          + '(' + field + ');'
        )
      await self._database.commit()

  def find(self, query=None, project=None, **kwargs):
    self._current_statement = 'SELECT '
    if kwargs.get('distinct'):
      self._current_statement += 'DISTINCT '
    if not project:
      self._current_statement += '* '
    else:
      for field in project:
        self._current_statement += field + ','
    self._current_statement = self._current_statement[
                              :-1] + ' FROM ' + self._table.table_name
    self._current_statement += self.concat_where(query)
    return self

  def limit(self, size):
    if not self._current_statement: return None
    self._current_statement += ' LIMIT ' + str(size)
    return self

  def order_by(self, order_by, order):
    if not self._current_statement: return None
    self._current_statement += ' ORDER BY ' + order_by + ' '
    if isinstance(order, int):
      order = 'DESC' if order < 0 else 'ASC'
    self._current_statement += order + ' '
    return self

  def group_by(self, fields):
    if not self._current_statement: return None
    self._current_statement += ' GROUP BY '
    for field in fields:
      self._current_statement += field + ','
    self._current_statement = self._current_statement[:1]
    return self

  def insert(self, obj):
    self._current_statement = 'INSERT INTO ' + self._table.table_name + '('
    for field in obj.keys():
      self._current_statement += field + ','
    self._current_statement = self._current_statement[:-1] + ') VALUES ('
    for val in obj.keys():
      self._current_statement += val + ','
    self._current_statement = self._current_statement[:-1] + ')'
    return self

  def update(self, obj, query=None):
    self._current_statement = 'UPDATE ' + self._table.table_name
    for field, val in obj.items():
      self._current_statement += field + '=' + val + ','
    self._current_statement = self._current_statement[:-1] + ' '
    self._current_statement += self.concat_where(query)
    return self

  def remove(self, query=None):
    self._current_statement = 'DELETE FROM ' + self._table.table_name
    self._current_statement += self.concat_where(query)
    return self

  def distinct(self, project):
    return self.find(None, project, distinct=True)

  async def exec(self):
    if not self._current_statement: return None
    self._current_statement += ';'
    async with self._database:
      cur = await self._database.execute(self._current_statement)
      result = await cur.fetchall()
      await cur.close()
      return result

  @staticmethod
  def concat_where(query):
    if not query: return ''
    statement = ' WHERE '
    if isinstance(query, list):
      for sq in query:
        for field, op in sq.items():
          statement += field + str(op) + ' AND'
        statement = statement[:-3]
        statement += ' OR '
      statement = statement[:-3]
    else:
      for field, op in query.items():
        statement += field + str(op) + ' AND'
      statement = statement[:-3]
    return statement

class Database(object):
  connection = None

  @staticmethod
  async def create_table(model):
    table = Table(model, model.table_name)
    table_wrapped = TableWrapped(Database.connection, table)
    # ensure table exists
    await table_wrapped.create_table()

  @staticmethod
  def connect(db_uri):
    Database.connection = aiosqlite.connect(db_uri)
