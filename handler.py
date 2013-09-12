import json
import urllib
import util
import ocr

class Handler:
  def __init__(self,req):
    self.req = req

  def handle(self):

    params = util.parsePostData(self.req.data)
    data    = urllib.unquote(params['imgBin'])
    binary  = data.replace('data:image/png;base64,','')
    text = ocr.from_binary(binary)

    body = json.dumps({'result' : text })
    return (body,200)
