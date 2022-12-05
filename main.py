from flask import (
  Flask, 
  jsonify,
  abort,
  make_response,
  request,
  url_for
)
import Functions
from Globals import Global

if __name__ == '__main__':
    Global.app.run(debug=True)