import ocr,base64,sys

def get_fpath():
  if len(sys.argv) < 2:
    print("[WARNING] give file path in args")
    print("[USAGE]   ex) `python tdriver sample/b64sample001.txt`")
    exit(1)
  return sys.argv[1]

def main():
  file_path = get_fpath()
  b64str = open(file_path,'r').read()
  txt = ocr.from_binary(b64str, debug=True)
  print("THIS IS RESULT  : " + txt)

if __name__ == '__main__':
  main()
