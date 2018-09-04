import codecs
import json
from os import path
import attr

CONFIG_BASE = path.join(path.dirname(path.dirname(path.abspath(__file__))),
                        'configs/')

@attr.s
class Config(object):
  env = ''
  app_name = ''
  db_uri = ''

  @staticmethod
  def get(env: str = 'dev'):
    with codecs.open(CONFIG_BASE + env + '.json', 'r') as rf:
      _config = json.load(rf)
      Config.env = env
      Config.db_uri = _config.get('db_uri')
      Config.app_name = _config.get('app_name')
    return _config
