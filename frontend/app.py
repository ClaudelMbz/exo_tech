import streamlit as st
import requests
import json
import os


backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

def main():
    st.set_page_config(page_title="CV Extractor")

    st.title("CV Extractor")
    if 'data_cv' not in st.session_state:
        st.session_state['data_cv'] = None
    menu = ["Upload", "Result"]
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == "Upload":
        
        pdf_docx_file = st.file_uploader('Upload your CV', type=["pdf", "docx"])
        if st.button("Analyser le CV") :
            if pdf_docx_file is not None:
                # st.write(type(pdf_docx_file))
                # st.write(dir(pdf_docx_file))
                file_details = {"filename" : pdf_docx_file.name,
                                "filetype" : pdf_docx_file.type,
                                "filesize": pdf_docx_file.size }
                st.write(file_details)
                try:
                    # Préparation du dictionnaire pour l'envoi
# 'file' est le nom du champ attendu par FastAPI (file: UploadFile)
                    files = {"file": (pdf_docx_file.name, pdf_docx_file.getvalue(), pdf_docx_file.type)}

                    # Envoi de la requête
                    response = requests.post(f"http://{backend_url}/api/v1/upload-cv", files=files)
                    if response.status_code == 200:
                        st.success("Succes de l'analyse !")
                        st.session_state['data_cv'] = response.json().get("donnees")                        
                    else:
                        st.error("Erreur dans l'analyse")
                except Exception as e:
                    st.error(f"Backend non connecté : {e}") 
                

                
        
    else:          
        if st.session_state['data_cv'] :
                            st.subheader("Vérification des informations")
                            data_cv = st.session_state['data_cv']

                            lastnamemd = st.text_input("Nom", value=data_cv.get("nom"))
                            firstnamemd = st.text_input("Prénom", value=data_cv.get("prenom")) 
                            emailmd = st.text_input("Email", value=data_cv.get("email")) 
                            phonemd = st.text_input("Telephone", value=data_cv.get("telephone")) 
                            degreemd = st.text_input("Diplome", value=data_cv.get("diplome")) 

                            json_fin = {
                                "nom" : lastnamemd,
                                "prenom" : firstnamemd,
                                "email" : emailmd,
                                "telephone" : phonemd,
                                "diplome" : degreemd,
                            }

                            st.download_button(
                                label="Télécharger le JSON final",
                                data=json.dumps(json_fin, indent=4),
                                file_name=f"cv_{firstnamemd}.json",
                                mime="application/json"
                                )
        else:
            st.warning("Aucun CV analysé. Rendez-vous dans le Menu Upload.")


if __name__ == '__main__' :
    main()



