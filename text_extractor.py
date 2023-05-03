from PIL import Image
from pytesseract import pytesseract
import enum

class Language(enum.Enum):
    ENG = 'eng'

class ImageReader:

    def __init__(self):
        path = r'C:\Users\Swaraj\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = path

    
    def extract_text(self):
        img = Image.open('./Images/screenshot.png')
        extracted_text = pytesseract.image_to_string(img, lang='eng')
        return extracted_text




