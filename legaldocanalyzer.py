import re
import nltk
from PyPDF2 import PdfFileReader
import docx
import os

# Load NLTK resources
nltk.download('punkt')

def analyze_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PdfFileReader(f)
        text = ""
        for page in range(reader.numPages):
            text += reader.getPage(page).extract_text()
        return text

def analyze_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

def check_sensitive_info(text):
    patterns = {
        'SSN': r'\b\d{3}-\d{2}-\d{4}\b',
        'Credit Card': r'\b\d{4} \d{4} \d{4} \d{4}\b',
        'Email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    }
    results = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            results[key] = matches
    return results

def analyze_document(file_path):
    if file_path.endswith('.pdf'):
        text = analyze_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = analyze_docx(file_path)
    else:
        raise ValueError('Unsupported file type')

    sensitive_info = check_sensitive_info(text)
    return sensitive_info

if __name__ == "__main__":
    file_path = input("Enter the document file path: ")
    if not os.path.exists(file_path):
        print("File does not exist.")
    else:
        sensitive_info = analyze_document(file_path)
        if sensitive_info:
            print("Sensitive information found:")
            for key, matches in sensitive_info.items():
                print(f"{key}: {', '.join(matches)}")
        else:
            print("No sensitive information detected.")
