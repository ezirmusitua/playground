from sanic import Blueprint
from sanic.response import text
from sanic.views import HTTPMethodView

class SimpleView(HTTPMethodView):

  async def get(self, request):
    return text('I am get method')

  async def post(self, request):
    return text('I am post method')

  async def put(self, request):
    return text('I am put method')

  async def patch(self, request):
    return text('I am patch method')

  async def delete(self, request):
    return text('I am delete method')

home_bp = Blueprint('home', url_prefix='home')
home_bp.add_route(SimpleView.as_view(), '/')
