import codecs
import json
from os import path
import attr

CONFIG_BASE = path.join(path.dirname(path.dirname(path.abspath(__file__))),
                        'configs/')

@attr.s
class Config(object):
  env = attr.ib(type=str)
  config = attr.ib(type=dict, factory=dict, repr=False, hash=False)
  app_name = attr.ib(init=False, type=str)
  db_uri = attr.ib(init=False, type=str)
  instance = None

  def __new__(cls, env: str, config: dict):
    if not Config.instance:
      Config.instance = object.__new__(cls)
      Config.instance.env = env
      Config.instance.config = config
    return Config.instance

  def __attrs_post_init__(self):
    self.app_name = self.config.get('app_name', __file__)
    self.db_uri = self.config.get('db_uri')

  @staticmethod
  def get(env: str = 'dev'):
    with codecs.open(CONFIG_BASE + env + '.json', 'r') as rf:
      _config = json.load(rf)
      Config(env, _config)
    return _config
