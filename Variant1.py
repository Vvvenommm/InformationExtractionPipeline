import re
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO
from utils.FileWriter import write_to_file


def protect_and_clean(text):
    # pattern to identiy ECSS-Standards
    ecss_pattern = re.compile(r'ECSS-[A-Z]-[A-Z]{2}-\d{2}(?:-\d{2,})?\.?')
    
    # find all matching patterns
    ecss_matches = ecss_pattern.findall(text)

    # replace found pattern with placeholder
    placeholders = {f"PLACEHOLDER_{i}": match for i, match in enumerate(ecss_matches)}

    for placeholder, original in placeholders.items():
        text = text.replace(original, placeholder)
    
    #print(text)

    # Removal of ECSS-Q-ST-10C Rev.1 Muster
    text = re.sub(r'ECSS-Q-ST-10C Rev\.1', '', text)

    # Removal of date
    text = re.sub(r'\d{1,2}\s+[A-Za-z]+\s+\d{4}', '', text)

    # Removal of annotations, which are not following on Q- for standards with Q-
    text = re.sub(r'(?<!Q-)\b\d+(\.\d+)*\b', '', text)

    # Removal of annotations like a., b., c., d.
    text = re.sub(r'\b[a-zA-Z]\.\s*', '', text)

    # Removal of bullet points
    text = re.sub(u'\uf0b7', '', text)

    # Removal of isolated bullet points
    text = re.sub(r'^\s*\.\s*$', '', text, flags=re.MULTILINE)
    
    # restore ECSS-Standards with placeholders to original string
    for placeholder, original in placeholders.items():
        text = text.replace(placeholder, original)

    return text

if __name__ == '__main__':
    print('Text Extraction starting\n')
    with open('Standards/ECSS-Q-ST-10C-Rev.1.pdf', 'rb') as in_file:
        output_string = StringIO()
        laparams = LAParams(word_margin=0.1, line_margin=1, boxes_flow=1)  # LAParams-Objekt für Layout-Analyse
        # Text extraction with layout-analysis
        extract_text_to_fp(in_file, output_string, laparams=laparams, page_numbers=set([7,8,9,10,11,12,13,14,15,16,17,18]))
        extracted_text = output_string.getvalue()
    
    #extracted_text = extract_text('ECSS-Q-ST-10C-Rev.1.pdf', page_numbers=set([7,8,9,10,11,12,13,14,15,16,17,18]))

    # Bereinigung durchführen
    cleaned_text = protect_and_clean(extracted_text)

    # write extracted text to file
    write_to_file("Variant1-RegExpOnly.txt", cleaned_text)
