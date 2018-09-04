'''
Should define in format
{
  before_server_start= {

    _main: listener,

    <bp_name>: listener,

  }

}

before_server_start is the event name

_main means apply to app
'''
from listeners.prepare_database import prepare_database

listeners = dict(
  before_server_start=dict(
    _main=[prepare_database]
  )
)
