from PIL import Image, ImageFilter, ImageOps
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    image = image.convert("L")
    image = ImageOps.invert(image)
    image = image.filter(ImageFilter.SHARPEN)
    return image

def perform_ocr(image_path):
    image = Image.open(image_path)
    image = preprocess_image(image)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    image_path = './news.png'
    result = perform_ocr(image_path)
    print("OCR Result:")
    print(result)
