import streamlit as st
import streamlit.components.v1 as components
from tastranslation.translate import translate

# --- Title ---
st.title("📖 Serbian Reading App")

# --- Upload Text File ---
uploaded_file = st.file_uploader("Загрузите .txt файл книги", type="txt")

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")

    # Display text in a read-only text area
    st.write("📜 Текст:")
    st.text_area("text_area", text, height=300, key="full_text", disabled=True)

    # JavaScript to get selected text
    js_code = """
    <script>
    function getSelectionText() {
        var text = "";
        if (window.getSelection) {
            text = window.getSelection().toString();
        } else if (document.selection && document.selection.type != "Control") {
            text = document.selection.createRange().text;
        }
        document.getElementById("selected_text").value = text;
    }
    document.addEventListener("mouseup", getSelectionText);
    </script>
    <input type="text" id="selected_text" name="selected_text" style="width:100%" readonly>
    """
    components.html(js_code, height=50)

    # Get the highlighted text
    selected_text = st.text_input("Выделенный текст", "")

    # Translate when the button is clicked
    if st.button("Перевести"):
        if selected_text.strip():
            response = translate(selected_text, source_lang='sr', target_lang='en')
            st.write("📝 Оригинал:")
            st.info(selected_text)
            st.write("📝 Перевод:")
            st.info(response['response']['translated_text'])
        else:
            st.warning("Выберите текст для перевода!")