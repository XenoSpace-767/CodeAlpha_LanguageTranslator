import os
from gtts import gTTS
import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit Page Config
st.set_page_config(
    page_title="AI Language Translator", page_icon="🌐", layout="centered"
)

st.title("🌐 AI Language Translation Tool")
st.write(
    "Translate text into multiple languages instantly with speech synthesis."
)

# Supported Languages Mapping
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Hindi": "hi",
}

# UI Layout: Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox(
        "Source Language",
        options=["Auto Detect"] + list(LANGUAGES.keys()),
        index=0,
    )

with col2:
    target_lang_name = st.selectbox(
        "Target Language", options=list(LANGUAGES.keys()), index=1
    )

# Input Text Area
source_text = st.text_area(
    "Enter text to translate:",
    height=150,
    placeholder="Type or paste your text here...",
)

# Translation Processing
if st.button("Translate", type="primary", use_container_width=True):
    if not source_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        try:
            # Map selected language names to ISO codes
            source_code = (
                "auto"
                if source_lang_name == "Auto Detect"
                else LANGUAGES[source_lang_name]
            )
            target_code = LANGUAGES[target_lang_name]

            # Perform translation
            translator = GoogleTranslator(
                source=source_code, target=target_code
            )
            translated_text = translator.translate(source_text)

            # Display Translated Text Output
            st.success("Translation Complete!")
            st.subheader(f"Output ({target_lang_name}):")
            st.code(translated_text, language=None)

            # Text-to-Speech Generation
            tts = gTTS(text=translated_text, lang=target_code, slow=False)
            audio_file = "translated_audio.mp3"
            tts.save(audio_file)

            # Audio Player
            st.audio(audio_file, format="audio/mp3")

        except Exception as e:
            st.error(f"An error occurred during translation: {str(e)}")