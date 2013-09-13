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
  img =  Image.open(StringIO(decoded), "r")

  # --- this is lab ---
  # try to crop
  print(img.size)
  box = (200,360,600,480)
  img2 = img.crop(box)
  print(img2.size)
  # --- END lab ---

  """ ValueError: conversion from RGB to BMP not supported """
  # img = img.convert('BMP')
  """ ValueError: conversion from RGB to PNG not supported """
  # img = img.convert('PNG')
  """ IOError: cannot write mode RGBA as BMP """
  # img = img.convert()

  txt = tool.image_to_string(img,lang=lang,builder=builder)

  return txt
