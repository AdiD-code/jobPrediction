import os
import PyPDF2
import pytesseract
from pdf2image import convert_from_path

# Retrieve the Poppler bin path from environment variable
poppler_path = os.getenv('POPPLER_BIN', '')  # Default to '' if not set

# Specify the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        # Attempt to extract text using PyPDF2
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in range(len(reader.pages)):
                text += reader.pages[page].extract_text()
    except Exception as e:
        print(f"Error extracting text with PyPDF2: {e}")

    # Fallback to OCR if PyPDF2 fails or produces poor results
    if not text.strip():
        print("Falling back to OCR for text extraction.")
        # Use Poppler tools from the environment variable
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        text = ''
        for image in images:
            text += pytesseract.image_to_string(image)

    return text

if __name__ == "__main__":
    pdf_path = "sample_resume.pdf"
    print(extract_text_from_pdf(pdf_path))
