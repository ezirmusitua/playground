from .dispatcher import Dispatcher
from .utilities import exit

def start_terminal():
  dispatcher = Dispatcher()
  while True:
    try:
      dispatcher.read()
    except KeyboardInterrupt:
      exit()
