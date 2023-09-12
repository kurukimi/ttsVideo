from PIL import Image
import cv2
from pytesseract import pytesseract
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import numpy as np

def preprocess_finale(im):

    im = cv2.bilateralFilter(im,9,75,75)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    return im

def get_text_from_image(path: str) -> str:
    img = np.array(Image.open(path))
    im = preprocess_finale(img)
    cv2.imshow("f", im)
    cv2.waitKey(0)
    text = pytesseract.image_to_string(im)
    return text
    

if __name__ == "__main__":
    print(get_text_from_image("test.jpg"))