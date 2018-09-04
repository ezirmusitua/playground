from sanic import Sanic

from config import Config

LISTENER_EVENTS = [
  'before_server_start',
  'after_server_start',
  'before_server_stop',
  'after_server_stop'
]

def create_app(middlewares: dict, listeners: dict, blueprints: dict, env: str):
  config = Config.get(env)
  app = Sanic(config['app_name'])
  app.config.from_object(config)
  for middleware in middlewares:
    app.register_middleware(middlewares[0], middleware[1])
  for event in LISTENER_EVENTS:
    # NOTE: listener in format (event, event_handlers)
    print(event)
    for name in listeners.get(event, dict()):
      target = None
      if name == '_main':
        target = app
      elif blueprints.get(name):
        target = blueprints.get(name)
      for listener in listeners.get(event)[name]:
        target.listeners[event].append(listener)
  for name in middlewares:
    target = None
    if name == '_main':
      target = app
    elif blueprints.get(name):
      target = blueprints.get(name)
    for middleware in middlewares[name]:
      target.register_middleware(middleware[0], middleware[1])

  for blueprint in blueprints.values():
    # NOTE: blueprint in format (blueprint, blueprint options)
    app.blueprint(blueprint[0], **blueprint[1])
  return app
