# TODO : Refactor
# TODO : Security
# TODO : Content-Type : application/json

# Python Version 2.6.6

# --- modules
from flask import Flask
from flask import request
import urllib

# --- my modules
import conf
import ocr

def parsePostData(datastr):
  res = {}
  for kv in datastr.split('&'):
    (k,v) = kv.split('=')
    res[k] = v
  return res

app = Flask(__name__)

@app.route("/")
def index():
  return "This GET '/'"

@app.route('/upload', methods=['POST'])
def upload_file():

  if request.method != 'POST':
    return 'Method must be "POST"'

  if request.data is not None:
    params = parsePostData(request.data)

  data    = urllib.unquote(params['imgBin'])
  binary  = data.replace('data:image/png;base64,','')

  txt = ocr.from_binary(binary)

  if txt:
    return txt

  return "Saved?"

@app.route('/check', methods=['GET'])
def check():
  return "<img src='./uploaded_file.png'>";

if __name__ == "__main__":
  app.run(host=conf.host,port=conf.port)
