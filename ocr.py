# --- OCR ---
from PIL import Image
from PIL import ImageEnhance
from lib import pyocr
from lib.pyocr import builders
from StringIO import StringIO
import base64,re

# settings
tools = pyocr.get_available_tools()
tool = tools[0]
lang = 'eng'
builder = pyocr.builders.TextBuilder()

def is_correct(text):#bool
  correct_pattern = r'^[0-9]{2}:[0-9]{2}:[0-9]{2}$'
  if re.search(correct_pattern, text) is None:
    return False
  return True

def contrast_loop(img):# string
  for rate in range(10):
    enhancing = ImageEnhance.Contrast(img)
    img = enhancing.enhance(2**rate)
    txt = tool.image_to_string(img,lang=lang,builder=builder)
    if is_correct(txt):
      return txt
  return txt

def sharpness_loop(img):# string
  for rate in range(10):
    enhancing = ImageEnhance.Sharpness(img)
    img = enhancing.enhance(1/(2**rate))
    txt = tool.image_to_string(img,lang=lang,builder=builder)
    if is_correct(txt):
      return txt
  return txt

def from_binary(binary, debug=False):
  decoded = base64.b64decode(binary)
  img =  Image.open(StringIO(decoded), "r")


  # AT FIRST : try raw image
  txt = tool.image_to_string(img,lang=lang,builder=builder)
  if debug:
    print("RawImage\t: " + txt)
  if is_correct(txt):
    return txt

  # Basically, convert to monocolor
  img = img.convert("L")
  txt = tool.image_to_string(img,lang=lang,builder=builder)
  if debug:
    print("ConvertL\t: " + txt)
  if is_correct(txt):
    return txt

  # Basic enhancement
  enhancing = ImageEnhance.Contrast(img)
  img = enhancing.enhance(4)
  enhancing = ImageEnhance.Sharpness(img)
  img = enhancing.enhance(1/4)
  txt = tool.image_to_string(img,lang=lang,builder=builder)
  if debug:
    print("BasicEnhance\t: " + txt)
  if is_correct(txt):
    return txt

  # Sharpness Loop
  txt = sharpness_loop(img)
  if is_correct(txt):
    return txt

  # Cotrast Loop
  txt = contrast_loop(img)
  if is_correct(txt):
    return txt

  # Finally
  return txt
