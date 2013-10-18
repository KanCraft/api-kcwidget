import ocr,base64,sys,re,os

def parse_arg():
  res = {'file':'all'}
  if '--file' in sys.argv:
    i = sys.argv.index('--file')
    if len(sys.argv) < i + 1:
      exit(1)
    res['file'] = sys.argv[i + 1]
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
