
def parsePostData(datastr):
  res = {}
  for kv in datastr.split('&'):
    (k,v) = kv.split('=')
    res[k] = v
  return res
