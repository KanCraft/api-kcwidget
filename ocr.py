# --- OCR ---
from PIL import Image
from PIL import ImageEnhance
from lib import pyocr
from lib.pyocr import builders
from StringIO import StringIO
import base64

def from_binary(binary, debug=False):

  # settings
  tools = pyocr.get_available_tools()
  tool = tools[0]
  lang = 'eng'
  builder = pyocr.builders.TextBuilder()

  decoded = base64.b64decode(binary)
  img =  Image.open(StringIO(decoded), "r")

  txt = tool.image_to_string(img,lang=lang,builder=builder)
  if debug:
    print("RawImage\t: " + txt)
  if txt != "":
    return txt

  img = img.convert("L")
  txt = tool.image_to_string(img,lang=lang,builder=builder)
  if debug:
    print("ConvertL\t: " + txt)
  if txt != "":
    return txt

  # ENHANCE CONTRAST
  enhancing = ImageEnhance.Contrast(img)
  img2 = enhancing.enhance(32)
  #img = img2
  txt = tool.image_to_string(img2,lang=lang,builder=builder)
  if debug:
    print("Contrast\t: " + txt)
  if txt != "":
    return txt

  # TODO: formatting should be by application
  enhancing = ImageEnhance.Sharpness(img)
  img3 = enhancing.enhance(1/16)
  txt = tool.image_to_string(img3,lang=lang,builder=builder)
  if debug:
    print("Sharpness\t: " + txt)

  return txt
