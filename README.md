Sure, here's a sample README file for your GitHub repository. This README will explain the purpose of your project, how to set it up, and how to use it.

```
# PDF OCR and Text Analysis

This project demonstrates how to perform Optical Character Recognition (OCR) on a PDF document and analyze the extracted text using spaCy. The project uses `pdf2image` to convert PDF pages to images, `easyocr` for OCR, and `spaCy` for natural language processing.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone the repository and install the required dependencies.

```
git clone https://github.com/yourusername/pdf-ocr-text-analysis.git
cd pdf-ocr-text-analysis
!apt-get install poppler-utils
pip install -r requirements.txt
```

## Usage

1. **Download the PDF file**:
   The script downloads a sample PDF file for demonstration purposes.

2. **Convert PDF to images**:
   The `pdf2image` library is used to convert PDF pages to images.

3. **Perform OCR**:
   The `easyocr` library is used to perform OCR on the images.

4. **Draw bounding boxes**:
   Bounding boxes are drawn around the detected text.

5. **Extract and print text**:
   Extracted text from the OCR results is printed.

6. **Analyze text with spaCy**:
   The extracted text is analyzed using spaCy to visualize named entities.

```
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
```

## Project Structure

```
pdf-ocr-text-analysis/
├── functionalSample.pdf
├── requirements.txt
├── README.md
└── main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

