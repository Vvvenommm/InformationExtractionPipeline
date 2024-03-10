import pytesseract
from pdf2image import convert_from_path

def convert_pdf_to_image():
    print('Conversion from PDF to Image starting\n')

    # Path of pdf file and tesseract executer
    pdf_path = '/Users/mustafanail/Documents/Programmierung/MasterThesis/InformationExtractionPipeline/Standards/ECSS-Q-ST-10C-Rev.1.pdf'
    pytesseract.pytesseract.tesseract_cmd = r'/Users/mustafanail/miniconda3/envs/inf_extr_pipeline/bin/tesseract'

    pages_to_extract = [7,8,9,10,11,12,13,14,15,16,17,18]

    # list for extracted pages 
    extracted_images = []

    # extract only selected pages
    for page_number in pages_to_extract:
        images = convert_from_path(pdf_path, first_page=page_number, last_page=page_number, dpi=300)
        extracted_images.extend(images)

    return extracted_images