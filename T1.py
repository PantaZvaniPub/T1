# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 17:10:37 2025

@author: A397778
"""

import streamlit as st
from tastranslation.translate import translate

result = translate('Tell me a joke about Cloudflare', source_lang='en', target_lang='fr')
print(result)

# --- Константы ---


# --- Загрузка текста ---
st.title("📖 Serbian Reading App")
uploaded_file = st.file_uploader("Загрузите .txt файл книги", type="txt")

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    lines = text.split("\n")

    selected_line = st.selectbox("Выберите строку для перевода", lines)

    if selected_line:
        st.write("📝 Оригинал:")
        st.info(selected_line)

        # --- Кнопка перевода ---
        if st.button("Перевести строку"):
            response = translate('Tell me a joke about Cloudflare', source_lang='en', target_lang='fr')
            if response.status_code == 200:
                translated = response.json()["data"]["translations"][0]["translatedText"]
                st.success(f"Перевод: {translated}")

                # Сохранение в сессии
                if "dictionary" not in st.session_state:
                    st.session_state["dictionary"] = []

                st.session_state["dictionary"].append({
                    "original": selected_line,
                    "translated": translated
                })

    # --- Показать словарь пользователя ---
    if "dictionary" in st.session_state and len(st.session_state["dictionary"]) > 0:
        st.subheader("📚 Мой словарь")
        for item in st.session_state["dictionary"]:
            st.write(f"• {item['original']} → {item['translated']}")