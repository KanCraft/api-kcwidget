import ocr,base64,sys,re,os

def parse_arg():
  res = {'file':'all','debug':False}
  if '--file' in sys.argv:
    i = sys.argv.index('--file')
    if len(sys.argv) < i + 1:
      exit(1)
    res['file'] = sys.argv[i + 1]
  if '--detail' in sys.argv:
    res['debug'] = True
  return res

def exec_by_file(fpath,debug):
  b64str = open(fpath,'r').read()
  txt = ocr.from_binary(b64str, debug=debug)
  print("THIS IS RESULT  : " + txt)

def main():
  args = parse_arg()
  if args['file'] == 'all':
    for f_name in os.listdir('./sample'):
      print("===== " + f_name + " =====")
      exec_by_file('./sample/' + f_name, args['debug'])
    return

  exec_by_file(args['file'], args['debug'])

if __name__ == '__main__':
  main()
