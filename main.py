import streamlit as st
st.set_page_config(
    page_title="IhateTool", 
    page_icon="💔",
    layout="wide"
    )

# Main function to handle navigation
def main():

    home_page = st.Page("tools/home.py", title="Home", icon="🏚️", url_path="/home", default=True)
    word_to_pdf_page = st.Page("tools/word_to_pdf.py", title="Word to PDF", icon=":material/file_present:", url_path="/word-to-pdf")
    merge_pdf_page = st.Page("tools/merge_pdf.py", title="Merge PDF", icon=":material/download:", url_path="/merge-pdf")
    pages = {
        "Document Converter": [
            home_page,
            word_to_pdf_page,
            merge_pdf_page,
        ],
    }

    pg = st.navigation(pages)
    st.logo("assets/imgs/ihatetool_logo.png")
    st.sidebar.write("Developed by [Gio](https://github.com/Tickets14)😫")
    st.sidebar.write("Version 1.0.0")
    
    pg.run()


if __name__ == "__main__":
    main()

