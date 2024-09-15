import streamlit as st
from streamlit_extras.grid import grid

# Define the different pages
def home():
    st.title("🎀Home Page")
    st.info(":red-background[***IHateTool***] is a versatile web application designed to handle a wide range of document format conversions. Whether you're converting DOCX to PDF, Excel to CSV, or other file formats, IHateTool makes it easy and efficient. It ensures secure, fast, and user-friendly processing, prioritizing privacy without relying on external services for file handling.")

    my_grid = grid(1, [1, 1, 1], 1, 1, vertical_align="center")

    # Row 1
    my_grid.subheader("Document Converter", anchor=False)
    # Row 2
    if my_grid.button("Word to PDF", use_container_width=True):
        st.switch_page("tools/word_to_pdf.py")
    my_grid.button("PDF to Word", use_container_width=True)
    my_grid.button("Merge PDF",use_container_width=True)

    # Row 3
    my_grid.subheader("Image Converter", anchor=False)

    # Row 4
    my_grid.markdown("<h5 style='text-align: center; color: gray;'>🌷🌸🌹Coming Soon🌺🌻🌼</h5>", unsafe_allow_html=True)


home()
