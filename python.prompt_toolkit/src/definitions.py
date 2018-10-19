from prompt_toolkit.completion import WordCompleter
from .installation import install_wsl, install_linux, install_docker
from .net import usenet
from .eosio import map_to_command
from .resource import show_resource
from .utilities import exit

BUILD_IN_VARIABLES = [
  'net:local',
  'net:mainnet',
  'net:cryptokylin',
  'net:jungle'
  'resource:keys',
  'resource:passwords'
]

COMMANDS = {
  'install_wsl'    : install_wsl,
  'install_linux'  : install_linux,
  'install_docker' : install_docker,

  'use'            : usenet,

  'show'           : show_resource,

  'exit'           : exit,

  'cleos'          : map_to_command('cleos'),
  'keosd'          : map_to_command('keosd'),
  'nodeos'         : map_to_command('nodeos'),
  'eosio-ranlib'   : map_to_command('eosio-ranlib'),
  'eosio-ar'       : map_to_command('eosio-ar'),
  'eosio-objdump'  : map_to_command('eosio-objdump'),
  'eosio-readelf'  : map_to_command('eosio-readelf'),
  'eosio-cc'       : map_to_command('eosio-cc'),
  'eosio-cpp'      : map_to_command('eosio-cpp'),
  'eosio-ld'       : map_to_command('eosio-ld'),
  'eosio-pp'       : map_to_command('eosio-pp'),
  'eosio-abigen'   : map_to_command('eosio-abigen'),
  'eosio-wasm2wast': map_to_command('eosio-wasm2wast'),
  'eosio-wast2wasm': map_to_command('eosio-wast2wasm'),
}

COMPLETER = WordCompleter(list(COMMANDS.keys()) + BUILD_IN_VARIABLES)
