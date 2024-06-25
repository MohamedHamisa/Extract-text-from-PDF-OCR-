# Install necessary libraries
!apt-get install poppler-utils
!pip install pdf2image
!pip install easyocr
!pip install spacy
!pip install wget

# Import libraries
from pdf2image import convert_from_path
import easyocr
import numpy as np
from PIL import ImageDraw, Image
import spacy
import wget

# Download the PDF file
url = 'https://writing.colostate.edu/guides/documents/resume/functionalSample.pdf'
wget.download(url, 'functionalSample.pdf')

# Convert PDF to images
images = convert_from_path('functionalSample.pdf')

# Display the first page of the PDF
display(images[0])

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Perform OCR on the first page
bounds = reader.readtext(np.array(images[0]), min_size=0, slope_ths=0.2, ycenter_ths=0.7, height_ths=0.6, width_ths=0.8, decoder='beamsearch', beamWidth=10)

# Function to draw bounding boxes
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

# Draw bounding boxes on the first page
image_with_boxes = draw_boxes(images[0], bounds)
display(image_with_boxes)

# Extract text from OCR results
text = '\n'.join([bound[1] for bound in bounds])
print(text)

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Process text with spaCy
doc = nlp(text)

# Visualize named entities
from spacy import displacy
displacy.render(doc, style='ent', jupyter=True)
