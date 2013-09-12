# TODO : Refactor
# TODO : Security
# TODO : Content-Type : application/json

# Python Version 2.6.6

# --- modules
from flask import Flask
from flask import request
from flask import make_response
import urllib
import json

# --- my modules
import conf
import ocr
import util

app = Flask(__name__)

@app.route("/")
def index():
  return "This GET '/'"

@app.route('/upload', methods=['POST'])
def upload_file():

  if request.method != 'POST':
    return 'Method must be "POST"'
 
  if request.data is not None:
    params = util.parsePostData(request.data)
 
  data    = urllib.unquote(params['imgBin'])
  binary  = data.replace('data:image/png;base64,','')
 
  txt = ocr.from_binary(binary)
 
  if txt:
    body = json.dumps({'result' : txt })
    resp = make_response(body, 200)
    return resp

  return "Saved?"

@app.route('/check', methods=['GET'])
def check():
  return "<img src='./uploaded_file.png'>";

if __name__ == "__main__":
  app.run(host=conf.host,port=conf.port)
