import pytesseract

def extract_text_from_image(extracted_images):
    print('Text Extraction from Image starting \n')
    
    extracted_text = ""
    for image in extracted_images:
        text = pytesseract.image_to_string(image)
        extracted_text += text

    return extracted_text