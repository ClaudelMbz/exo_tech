# CV Extractor 📄

Un outil automatisé pour l'extraction les données {nom, prenom, email, telephone, diplome} des CV au format PDF et DOCX. Ce projet utilise une approche basée sur des **Regex (expressions régulières)** pour garantir une extraction rapide et prévisible, sans dépendance à une IA externe.

## 🛠 Installation
### Prérequis

* **Python 3.11+**
* **Docker Desktop** (pour le lancement via conteneurs)
* Un environnement virtuel (recommandé)

### Configuration initiale
```bash
# Cloner le projet
git clone https://github.com/ClaudelMbz/exo_tech.git
cd cv-extractor

# Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate
.venv\Scripts\Activate.ps1  # Sur Windows

```

---

## 🚀 Lancement Local

Si vous souhaitez lancer les services sans Docker :

### 1. Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

```

*Le backend sera disponible sur `http://localhost:8000*`

### 2. Frontend (Streamlit)

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py

```

*L'interface sera disponible sur `http://localhost:8501*`
---

## 🐳 Lancement avec Docker
C'est la méthode recommandée pour garantir que tout fonctionne parfaitement.

```bash
cd docker
docker-compose up --build
```

**Accès aux services :**

* **Frontend :** `http://localhost:8501`
* **Documentation API (Swagger) :** `http://localhost:8000/docs`
---

## 📡 Exemples d'API
### Extraire les données d'un CV
**Endpoint :** `POST /api/v1/upload-cv`
**Exemple avec cURL :**
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/upload-cv' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@ton_cv.pdf'
```

**Réponse type (JSON) :**
```json
{
    "donnees": {
        "nom": "EL MOJAHID",
        "prenom": "SOUKAINA",
        "email": "soukainaelmojahid@outlook.fr",
        "telephone": "Null",
        "diplome": "master"
    }
}

```

---

## 📂 Structure du projet

* `backend/` : Logique FastAPI et scripts d'extraction (Regex).
* `frontend/` : Interface utilisateur Streamlit.
* `docker/` : Dockerfiles et configuration d'orchestration.
* `models/` : Modèles Pydantic pour la validation des données.

---
