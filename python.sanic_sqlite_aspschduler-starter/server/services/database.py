import attr

class Database(object):

  @classmethod
  def create_table(cls, model):
    table = Table(model, model.table_name)
    print(table)
    pass

@attr.s
class Table(object):
  _cls = attr.ib(init=True)
  table_name = attr.ib(type=str, hash=True)
  fields = attr.ib(type=dict, factory=dict)

  def __attrs_post_init__(self):
    self.fields = Table.generate_fields_info(self._cls)

  @staticmethod
  def generate_fields_info(_cls):
    fields = dict()
    for field in attr.fields(_cls):
      fields[field.name] = dict(name=field.name)
      # type info
      if field.type == str:
        fields[field.name]['type'] = 'TEXT'
      elif field.type == int:
        fields[field.name]['type'] = 'INTEGER'
      elif field.type == float:
        fields[field.name]['type'] = 'REAL'
      else:
        fields[field.name]['type'] = 'BLOB'
      for key in field.metadata:
        if key.lower() in ['unique', 'notnull', 'primary', 'index',
                           'foreign']:
          fields[field.name][key] = field.metadata[key]
    return fields
