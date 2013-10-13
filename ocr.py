# --- OCR ---
from PIL import Image
from PIL import ImageEnhance
from lib import pyocr
from lib.pyocr import builders
from StringIO import StringIO
import base64

def from_binary(binary):
  # settings
  tools = pyocr.get_available_tools()
  tool = tools[0]
  lang = 'eng'
  builder = pyocr.builders.TextBuilder()

  decoded = base64.b64decode(binary)
  img =  Image.open(StringIO(decoded), "r")

  # --- this is lab ---
  # ENHANCE CONTRAST
  enhancing = ImageEnhance.Contrast(img)
  img2 = enhancing.enhance(1.5)
  img = img2
  # --- END lab ---

  """ ValueError: conversion from RGB to BMP not supported """
  # img = img.convert('BMP')
  """ ValueError: conversion from RGB to PNG not supported """
  # img = img.convert('PNG')
  """ IOError: cannot write mode RGBA as BMP """
  # img = img.convert()

  txt = tool.image_to_string(img,lang=lang,builder=builder)

  return txt
