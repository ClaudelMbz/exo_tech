import re
import unicodedata

def clean_text(text: str) -> str:
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode("utf-8")
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    text = re.sub(r'\s+', ' ', text).strip()  
    return text

def extract_data(cleaned_text: str, uncleaned_text:str):

    email_pattern = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'
    email = re.search(email_pattern, cleaned_text)
    phone_pattern = r'(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}'
    phone = re.search(phone_pattern, cleaned_text)
    degree_pattern = r'(master|licence|bac|doctorat|bts|dut|ingenieur)'
    degree = re.search(degree_pattern, cleaned_text)
    name = uncleaned_text.split()
    firstname = name[0]
    lastname = name[1]
    if len(name[1]) <= 2:
        lastname = f"{name[1]} {name[2]}"
        
    return {
        "nom" : lastname,
        "prenom" : firstname,
        "email": email.group(0) if email else "Null",
        "telephone": phone.group(0) if phone else "Null",
        "diplome": degree.group(0) if degree else "Null",
    }

