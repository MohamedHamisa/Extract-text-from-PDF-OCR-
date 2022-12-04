!apt-get install poppler-utils
# free software utility library for rendering Portable Document Format (PDF) documents
!pip install pdf2image
!pip install easyocr

from pdf2image import convert_from_path
import easyocr
import numpy as np
import PIL
from PIL import ImageDraw
import spacy

reader = easyocr.Reader(['en'])

!wget https://writing.colostate.edu/guides/documents/resume/functionalSample.pdf

images = convert_from_path('functionalSample.pdf')

from IPython.display import display, Image
display(images[0])

bounds = reader.readtext(np.array(images[0]), min_size=0, slope_ths=0.2, ycenter_ths=0.7, height_ths=0.6, width_ths=0.8,decoder='beamsearch', beamWidth=10)
bounds
#draw boxes around the words
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(images[0], bounds)

bounds[1][1]

text=''
for i in range(len(bounds)):
  text = text + bounds[i][1] +'\n'

print(text)

nlp=spacy.load('en_core_web_sm')

doc = nlp(text)
from spacy import displacy

displacy.render(nlp(doc.text),style='ent', jupyter=True)


