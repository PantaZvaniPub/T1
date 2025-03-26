import streamlit as st
import streamlit.components.v1 as components
from tastranslation.translate import translate  # Import the translate function

def main():
    # Set up the Streamlit app
    st.title('Text File Translation')

    # Upload the .txt file
    uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])

    if uploaded_file is not None:
        # Read the uploaded file
        text = uploaded_file.read().decode('utf-8')
        st.subheader('Text Content')
        st.text_area("Text content of the file:", text, height=300)

if __name__ == "__main__":
    main()
