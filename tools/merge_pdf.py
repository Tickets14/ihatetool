import streamlit as st
from PyPDF2 import PdfMerger
import os

def merge_pdf():
    st.title("🔗:blue[Merge] PDF Files", anchor=False)

    col1, col2 = st.columns(2)
    with col1:
        expander = st.expander("**What is this?**", expanded=True, icon="🤔")
        expander.info('''
            This tool allows you to merge multiple :blue[**PDF**] files into a single file. 
            Just upload your PDF files and click merge!
        ''')
    with col2:
        expander = st.expander("**Reminders**", expanded=True, icon="💡")
        expander.info("Ensure all uploaded files are :blue[**PDF**] format. For any issues, please contact the developer.")

    # Upload multiple files
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        # Check if the user uploaded more than one PDF file
        if len(uploaded_files) < 2:
            st.error("Please upload at least two PDF files to merge.")
            return

        st.info(f"{len(uploaded_files)} PDF files uploaded.")

        # Initialize PdfMerger
        merger = PdfMerger()

        # Add each uploaded PDF file to the merger
        for uploaded_file in uploaded_files:
            merger.append(uploaded_file)

        # Create a temporary file to hold the merged PDF
        output_path = "merged_output.pdf"

        # Output the merged PDF into a file
        with open(output_path, "wb") as output_pdf:
            merger.write(output_pdf)
            merger.close()

        # Read the merged file back as bytes for download
        with open(output_path, "rb") as output_pdf:
            merged_pdf_bytes = output_pdf.read()

        # Allow the user to download the merged PDF file
        st.download_button(
            label="Download Merged PDF",
            data=merged_pdf_bytes,
            file_name="merged_ihatepdf.pdf",
            mime="application/pdf"
        )

        # After the download button, delete the temporary file
        if os.path.exists(output_path):
            try:
                os.remove(output_path)
            except Exception as cleanup_error:
                st.error(f"Error cleaning up temporary file: {cleanup_error}")

merge_pdf()