import streamlit as st
import requests
import os

def word_to_pdf():
    is_loading = False

    st.title("🎀:blue[**Word**] to :red[**PDF**] Converter", anchor=False)

    col1, col2 = st.columns(2)
    with col1:
        expander = st.expander("**What is this?**", expanded=True, icon="🤔")
        expander.info('''
            This tool allows you to upload :blue[**Word**] files and convert them to :red[**PDF**] format.
            It's fast, easy, and free!
        ''')
    with col2:
        expander = st.expander("**Reminders**", expanded=True, icon="💡")
        expander.info("Please note that this tool is not perfect and may not work for all :blue[**Word**] files. If you encounter any issues, please contact the developer.")
    

    # File upload
    uploaded_file = st.file_uploader("Upload a DOCX file", type=["docx"])

    if uploaded_file is not None:
        with st.spinner("Converting to PDF..."):
            is_loading = True

        # Extract the base name of the uploaded file (without extension)
        file_name_without_ext = os.path.splitext(uploaded_file.name)[0]
        # Create a new filename for the PDF
        pdf_file_name = f"{file_name_without_ext}_ihatepdf.pdf"
        
        # Send the uploaded file to the FastAPI backend
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        }
        response = requests.post("https://ihatetool-boc4v71ug-tickets-projects-05435495.vercel.app/docs/word-to-pdf", files=files)

        if response.status_code == 200:
            is_loading = False
            filename = response.headers.get("filename")
            # Create a download button for the response PDF
            st.download_button(
                label="Download PDF",
                data=response.content,
                file_name=filename,
                mime="application/pdf"
            )
        else:
            st.error("Error converting file: " + response.text)
            is_loading = False


word_to_pdf()