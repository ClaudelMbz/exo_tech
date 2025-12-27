from pydantic import BaseModel, EmailStr
from typing import Optional

class CVData(BaseModel):
    nom: str
    prenom: str
    email: str 
    telephone: str
    diplome: str


class CVResponse(BaseModel):
    status: str
    filename: str
    donnees: CVData 