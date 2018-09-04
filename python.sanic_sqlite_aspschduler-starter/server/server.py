from middlewares import middlewares
from listeners import listeners
from blueprints import blueprints
from services.app import create_app

if __name__ == '__main__':
  app = create_app(middlewares, listeners, blueprints, 'dev')
  app.run(host='0.0.0.0', port=8081, debug=True)
