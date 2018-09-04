import attr

@attr.s
class _User(object):
  username = attr.ib(type=str, metadata={'primary': True})
  age = attr.ib(type=str)
  table_name = 'User'
