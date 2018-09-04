from sanic import Sanic

from config import Config

LISTENER_EVENTS = [
  'before_server_start',
  'after_server_start',
  'before_server_stop',
  'after_server_stop'
]

def create_app(middlewares: list, listeners: dict, blueprints: list, env: str):
  config = Config.get(env)
  app = Sanic(config['app_name'])
  app.config.from_object(config)
  for middleware in middlewares:
    app.register_middleware(middlewares[0], middleware[1])
  for event in LISTENER_EVENTS:
    # NOTE: listener in format (event, event_handlers)
    for listener in listeners.get(event, []):
      app.listeners[event].append(listener)
  for blueprint in blueprints:
    # NOTE: blueprint in format (blueprint, blueprint options)
    app.blueprint(blueprint[0], **blueprint[1])
  return app
