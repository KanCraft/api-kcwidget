import json
import urllib
import util
import ocr
import re

class Handler:

  status = 200
  body   = {
    'result'  : '',
    'message' : ''
  }

  def __init__(self,req):
    self.req = req

  def finish(self):
    bodystr = json.dumps(self.body)
    return (bodystr, self.status)

  def validateRequest(self):
    if self.req.method != 'POST':
      self.body['message'] = 'Method must be POST';
      self.status = 405
      return False
    return True

  def validateParams(self,params):
    if len(params) < 1:
      self.body['message'] = 'Missing parameter "data"'
      self.status = 400
      return False
    if 'imgBin' not in params:
      self.body['message'] = 'Missing parameter "data.imgBin"'
      self.status = 400
      return False
    return True

  def validateData(self,data):
    if re.match('data:image/png;base64,',data) is None:
      self.body['message'] = 'Wrong data format. Required "base64 encoded image/png"'
      self.status = 400
      return False
    return True

  def handle(self):

    if not self.validateRequest():
      return self.finish()

    params = util.parsePostData(self.req.data)
    if not self.validateParams(params):
      return self.finish()

    data = urllib.unquote(params['imgBin'])
    if not self.validateData(data):
      return self.finish()

    binary  = data.replace('data:image/png;base64,','')
    self.body['result'] = ocr.from_binary(binary)

    return self.finish()
