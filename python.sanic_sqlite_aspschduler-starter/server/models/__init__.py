from models.user import User

models = [User]

def register_models(database):
  for model in models:
    table = database.create_table(model)
    model._table = table
