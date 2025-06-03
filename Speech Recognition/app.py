import streamlit as st
import whisper
from utils import convert_audio_to_wav, LANGUAGES
from googletrans import Translator
import os

# -------------------------
# 1) Page config (MUST be first Streamlit command):
# -------------------------
st.set_page_config(page_title="🎙️ Whisper Transcriber + Translator", layout="centered")

# -------------------------
# 2) Load Whisper model (cached):
# -------------------------
@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

model = load_whisper()

# -------------------------
# 3) Initialize googletrans translator (cached):
# -------------------------
@st.cache_resource
def load_translator():
    return Translator()

translator = load_translator()

# -------------------------
# 4) UI elements:
# -------------------------
st.title("🗣️ Multilingual Speech Transcriber & Translator")
st.write("Upload an audio file and choose a target language to transcribe with Whisper and translate with Google Translate.")

# File uploader:
uploaded_file = st.file_uploader(
    "📁 Upload audio file (.wav, .mp3, .ogg, .flac, etc.)",
    type=["wav", "mp3", "ogg", "flac"]
)

# Language selector:
target_lang = st.selectbox(
    "🌐 Translate transcript to:",
    options=list(LANGUAGES.keys()),
    format_func=lambda code: LANGUAGES.get(code, code)
)

# -------------------------
# 5) When a file is uploaded:
# -------------------------
if uploaded_file:
    # Convert to WAV
    with st.spinner("🔄 Converting audio to WAV..."):
        wav_path = convert_audio_to_wav(uploaded_file)

    # Whisper transcription
    with st.spinner("🧠 Transcribing with Whisper..."):
        result = model.transcribe(wav_path)
        transcript = result.get("text", "")

    st.success("✅ Transcription Complete")
    st.subheader("📝 Transcript")
    st.text_area(" ", transcript, height=200)

    # Download button for original transcript
    st.download_button("💾 Download Transcript", transcript, file_name="transcript.txt")

    # Translation (if target != English)
    if target_lang != "en":
        with st.spinner(f"🌍 Translating to {LANGUAGES[target_lang]}..."):
            try:
                translated = translator.translate(transcript, src="en", dest=target_lang).text
            except Exception as e:
                translated = ""
                st.error(f"Translation failed: {e}")

        st.subheader(f"🗨️ Translated ({LANGUAGES[target_lang]})")
        st.text_area(" ", translated, height=200)
        st.download_button("💾 Download Translation", translated, file_name=f"translation_{target_lang}.txt")

    # Clean up temporary WAV
    os.remove(wav_path)
