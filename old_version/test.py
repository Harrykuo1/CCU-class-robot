from PIL import Image
import pytesseract

if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    img = Image.open('test.png')
    text = pytesseract.image_to_string(img)
    print(text)