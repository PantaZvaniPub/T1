# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 17:10:37 2025

@author: A397778
"""

import streamlit as st
from tastranslation.translate import translate



# --- Константы ---


# --- Загрузка текста ---
st.title("📖 Serbian Reading App")
uploaded_file = st.file_uploader("Загрузите .txt файл книги", type="txt")

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    lines = text.split("\n")
    st.text_area("Text content of the file:", text, height=300)

    selected_text = st.text_area("Выделенный текст", "")

    # Translate when the button is clicked
    if st.button("Перевести"):
        response = translate(selected_text, source_lang='sr', target_lang='en')
        st.write("📝 Оригинал:")
        st.info(selected_text)
        st.write("📝 Перевод:")
        st.info(response['response']['translated_text'])
