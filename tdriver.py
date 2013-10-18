import ocr,base64,sys,re,os

def parse_arg():
  res = {'file':''}
  for val in sys.argv:
    if re.search('=', val) is None:
      continue
    k,v = val.split('=')
    res[k] = v
  return res

def exec_by_file(fpath):
  b64str = open(fpath,'r').read()
  txt = ocr.from_binary(b64str, debug=True)
  print("THIS IS RESULT  : " + txt)

def main():
  args = parse_arg()
  if args['file'] == 'all':
    for f_name in os.listdir('./sample'):
      print("===== " + f_name + " =====")
      exec_by_file('./sample/' + f_name)
    return

  exec_by_file(args['file'])

if __name__ == '__main__':
  main()
