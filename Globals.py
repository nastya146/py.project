from flask import (
  Flask
)

class Global:
  app = Flask(__name__)
  users = dict()
  notebook = dict()
