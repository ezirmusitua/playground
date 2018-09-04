import attr

from services.database import TableWrapped

@attr.s
class Model(object):
  _table: TableWrapped = None

  def find(self, query, project):
    return self._table.find(query, project)

  def insert(self, obj):
    return self._table.insert(obj)

  def update(self, obj, query):
    return self._table.update(obj, query)

  def remove(self, query):
    return self._table.remove(query)

  def distinct(self, project):
    return self._table.distinct(project)
