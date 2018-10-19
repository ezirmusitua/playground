ENV = {
  'project_dir': '.',
  'network'    : 'http://localhost:8888'
}

def set_env(key, value):
  ENV.update({key: value})

def get_env(key):
  return ENV.get(key)

def print_env():
  print('= = = = = = = = = =' * 3)
  print('Project Directory: ', ENV['project_dir'])
  print('Network: ', ENV['network'])
  print('= = = = = = = = = =' * 3)
