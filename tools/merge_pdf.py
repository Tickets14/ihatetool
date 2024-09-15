import streamlit as st
from PyPDF2 import PdfMerger
import os
from utilities.datehelper import DateHelper

def merge_pdf():
    date_helper = DateHelper()
    current_date = date_helper.get_current_date()

    st.title("🔗:blue[Merge] PDF Files", anchor=False)

    col1, col2 = st.columns(2)
    with col1:
        expander = st.expander("**What is this?**", expanded=True, icon="🤔")
        expander.info('''This tool allows you to merge multiple :blue[**PDF**] files into a single file. 
            Just upload your PDF files and click merge!''')
    with col2:
        expander = st.expander("**Reminders**", expanded=True, icon="💡")
        expander.info("Please ensure that all uploaded files are in PDF format. Files in other formats will not be accepted. If you encounter any issues, please contact the developer for assistance.")

    # Upload files
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    # Enable or disable the submit button based on the number of uploaded files
    if uploaded_files and len(uploaded_files) >= 2:
        button_disabled = False
    else:
        button_disabled = True

    with st.form("my-form", clear_on_submit=True):
        submitted = st.form_submit_button(
            "Merge", disabled=button_disabled
        )
        if submitted:
            if not uploaded_files or len(uploaded_files) < 2:
                st.error("Please upload at least two PDF files.", icon="🚨")
                return

            st.info(f"{len(uploaded_files)} PDF files uploaded.")

            # Initialize PdfMerger
            merger = PdfMerger()

            # Add each uploaded PDF file to the merger
            for uploaded_file in uploaded_files:
                merger.append(uploaded_file)

            # Create a temporary file to hold the merged PDF
            output_path = f"merged_pdf_{current_date}.pdf"

            # Output the merged PDF into a file
            with open(output_path, "wb") as output_pdf:
                merger.write(output_pdf)
                merger.close()

            # Read the merged file back as bytes for download
            with open(output_path, "rb") as output_pdf:
                merged_pdf_bytes = output_pdf.read()

            st.download_button(
                label="Download Merged PDF",
                data=merged_pdf_bytes,
                file_name=output_path,
                mime="application/pdf",
                on_click=lambda: st.toast("PDF file downloaded!", icon="✅"),
            )

            # After the download button, delete the temporary file
            if os.path.exists(output_path):
                try:
                    os.remove(output_path)
                except Exception as cleanup_error:
                    st.error(f"Error cleaning up temporary file: {cleanup_error}")

merge_pdf()
