from functools import partial
from prompt_toolkit import prompt
from .definitions import COMPLETER, COMMANDS

class Dispatcher(object):
  cmd_prompt = partial(prompt, '$ > ', completer=COMPLETER)

  def read(self):
    input = self.cmd_prompt()
    Dispatcher.parse_input(input)

  @staticmethod
  def parse_input(command):
    parsed = command.split(' ')
    command = parsed[0]
    args = parsed[1:]
    command_func = COMMANDS.get(command)
    if not command_func:
      print('Not supported command: ', command)
    else:
      command_func(*args)
