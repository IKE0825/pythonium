from PIL import Image
import sys

import pyocr
import pdb

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))

pdb.set_trace()
txt = tool.image_to_string(
    Image.open(r'C:\Users\ec000248\Downloads\2019-12-14\ocr-test.png'),
    lang="jpn",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print( txt )

exit()