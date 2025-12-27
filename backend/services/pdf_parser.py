import pdfplumber
import io

def extractor_pdf(file_from_api):
    text = ""
    with pdfplumber.open(io.BytesIO(file_from_api)) as pdf:
        for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    return text
