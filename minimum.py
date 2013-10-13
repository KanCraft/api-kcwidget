# Python Version 2.6.6

# --- modules
from flask import Flask
from flask import request
from flask import make_response
import sys,re

# --- my modules
import conf
from handler import Handler

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
  (body, status) = Handler(request).handle()
  resp = make_response(body, status)
  resp.headers['Content-Type'] = 'application/json'
  return resp

if __name__ == "__main__":
  k, port = ('','')
  if len(sys.argv) > 1:
    if re.search('=', sys.argv[1]):
      k, port = sys.argv[1].split('=')
    if sys.argv[1] == 'debug':
      app.debug = True
  if k == 'port':
    app.run(host=conf.host,port=int(port))
  else:
    app.run(host=conf.host,port=conf.port)
