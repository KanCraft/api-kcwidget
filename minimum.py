# TODO : Refactor
# TODO : Security
# TODO : Content-Type : application/json

# Python Version 2.6.6

from flask import Flask
from flask import request

# --- OCR ---
from PIL import Image
import pyocr
import pyocr.builders

# --- StringIO ---
from StringIO import StringIO

# --- urllib
import urllib
import base64

# --- my module
from conf import *

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
  decoded = base64.b64decode(binary)

  img =  Image.open(StringIO(decoded))

  """ OCR  """
  tools = pyocr.get_available_tools()
  tool = tools[0]
  langs = tool.get_available_languages()
  txt = tool.image_to_string(img,
                            lang='eng',
                            builder=pyocr.builders.TextBuilder())
  if txt:
    return txt
  """ OCR END """

  return "Saved?"

@app.route('/check', methods=['GET'])
def check():
  return "<img src='./uploaded_file.png'>";

if __name__ == "__main__":
  app.run(host=host,port=port)
