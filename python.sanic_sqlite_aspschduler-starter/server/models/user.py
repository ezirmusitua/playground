import attr

from models.model import Model

@attr.s
class User(Model):
  username = attr.ib(type=str, metadata={'primary': True}, default='')
  age = attr.ib(type=str, default='')
  table_name = 'User'
