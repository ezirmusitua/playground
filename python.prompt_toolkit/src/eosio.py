def map_to_command(command):
  def cmd(*args):
    print('args: ', args)
    print('map to command: TODO: use subprocess to execute')
    if command == 'cleos':
      print('cleos command should wrap with used network')
    else:
      print('other eosio commands')
    return

  return cmd
