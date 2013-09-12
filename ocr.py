# --- OCR ---
from PIL import Image
import pyocr
import pyocr.builders
from StringIO import StringIO
import base64

def from_binary(binary):
  # settings
  tools = pyocr.get_available_tools()
  tool = tools[0]
  lang = 'eng'
  builder = pyocr.builders.TextBuilder()

  decoded = base64.b64decode(binary)
  img =  Image.open(StringIO(decoded))

  txt = tool.image_to_string(img,lang=lang,builder=builder)

  return txt
