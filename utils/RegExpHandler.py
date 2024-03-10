import re

def clean_text(extracted_text):
    # Remove ECSS-Q-ST-10C Rev.1 pattern
    pattern = re.compile(r'ECSS-Q-ST-10C Rev\.1', re.M)
    cleaned_text = pattern.sub('', extracted_text)

    # Remove Date
    cleaned_text = re.sub(r'\d{1,2}\s+[A-Za-z]+\s+\d{4}', '', cleaned_text)

    # Remove Chapter annotation
    #cleaned_text = re.sub(r'(?<!Q-)\b\d+(\.\d+)*\b', '', cleaned_text)

    # Remove annotations like a., b., c., d.
    cleaned_text = re.sub(r'\b[a-zA-Z]\.\s*', '', cleaned_text)

    # Remove long 'Bindestrich'
    cleaned_text = re.sub(r'—\s', '', cleaned_text)

    # Remove different kind of bullelt point after conversion "°"
    cleaned_text = re.sub(r'°\s', '', cleaned_text)

    # Remove bullet point
    #cleaned_text = re.sub(u'\uf0b7', '', cleaned_text)

    return cleaned_text