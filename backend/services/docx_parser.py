from docx import Document
import io

def extractor_docx(file_from_api : bytes) -> str:
    doc = Document(io.BytesIO(file_from_api))
    full_text = []

    for para in doc.paragraphs:
        if para.text:
            full_text.append(para.text) 

    return("\n".join(full_text))