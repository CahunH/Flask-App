from flask import flask
def create_app():
  app = Flask(_name_)
  from .routes import main
  app.register_blueprint(main)
  return app
