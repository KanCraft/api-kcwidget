import json

class Handler:
  def __init__(self,req):
    self.req = req
    print(self.req.method)

  def handle(self):
    body = json.dumps({'result' : 'hoge' })
    return (body,200)
