from .env import set_env

NETWORKS = {
  'LOCAL'      : 'net:local',
  'MAINNET'    : 'net:mainnet',
  'CRYPTOKYLIN': 'net:cryptokylin',
  'JUNGLE'     : 'net:jungle'
}

# TODO: add endpoint

NETWORK_ENDPOINTS = {
  NETWORKS['LOCAL']      : 'http://localhost:8888',
  NETWORKS['MAINNET']    : 'https://node.get-scatter.com:443',
  NETWORKS['CRYPTOKYLIN']: 'http://???.com:8888',
  NETWORKS['JUNGLE']     : 'http://???.com:8888'
}

def usenet(*args):
  if not args or len(args) == 0:
    print(
      'use command must have network parameter, for example: use net:mainnet'
    )
    return
  if args[0] not in list(NETWORKS.values()):
    print(args[0].strip(), ' is not a valid network(candidates: ',
          ','.join(list(NETWORKS.values())))
    return
  if args[0] == NETWORKS['LOCAL']:
    # TODO: check is localhost:8888 available
    pass
  set_env('network', NETWORK_ENDPOINTS[args[0]])
  print('Current network change to ', args[0], '[', NETWORK_ENDPOINTS[args[0]],
        ']')
