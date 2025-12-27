from fastapi import FastAPI, UploadFile, File, HTTPException
from services.docx_parser import extractor_docx
from services.pdf_parser import extractor_pdf
from services.extractor import clean_text, extract_data
from models.cv_result import CVResponse


app = FastAPI()

@app.post("/api/v1/upload-cv", response_model=CVResponse)
async def upload_cv(file: UploadFile = File(...)): 
    content = await file.read()
    
    if file.content_type == "application/pdf":
        text_from = extractor_pdf(content)        
    elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text_from = extractor_docx(content)
    else:
        if not text_from or text_from.strip() == "":
            raise HTTPException(
            status_code=400, 
            detail="Format non supporté"
        )

        raise HTTPException(status_code=400, 
                            detail="Fichier Vide")
    
        
    cleaned_text = clean_text(text_from)
    resultat = extract_data(cleaned_text, text_from)
    print(resultat["nom"])
    
    return {
        "status" : "success",
        "filename": file.filename,
        "donnees" : {
            "nom" : resultat["nom"],
            "prenom" : resultat["prenom"],
            "email" : resultat["email"],
            "telephone" : resultat["telephone"],
            "diplome" : resultat["diplome"]
        }    
    }