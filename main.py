from utils.PDFConverts import convert_pdf_to_image
from utils.ImageExtractor import extract_text_from_image
from utils.FileWriter import write_to_file
from utils.RegExpHandler import clean_text

    # -> important to get some special characters for the removal by RegExp
    #print(extracted_text.split())

def start_pipeline():
    print('Information Extraction Pipeline starting\n')

    # convert pdf to image with Tesseract OCR and return list of images
    extracted_images = convert_pdf_to_image()

    # convert image to text
    extracted_text = extract_text_from_image(extracted_images)

    # write extracted text to file
    write_to_file("Variant2-TesseractOCR-notCleaned.txt", extracted_text)

    # clean text with RegExp
    cleaned_text = clean_text(extracted_text)

    # write extracted text to file
    write_to_file("Variant2-TesseractOCR-cleaned.txt", cleaned_text)

    #nlp = spacy.load("en_core_web_sm") #loading the core englisch language

    # TODO - Segmentation and Tokenization


if __name__ == '__main__':
    print('Text Extraction starting\n')

    start_pipeline()


# Variant 1 - tested: Only RegExp -> Result is in ExtractedTextFromVariant1.txt
