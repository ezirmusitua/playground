import click
from .dispatcher import Dispatcher
from .utilities import exit
from .env import set_env, print_env

@click.command()
@click.option("--project", default='.', help="working directory")
def start_terminal(project):
  set_env('project_dir', project)
  print_env()
  dispatcher = Dispatcher()
  while True:
    try:
      dispatcher.read()
    except KeyboardInterrupt:
      exit()
