from pydub import AudioSegment
import tempfile

def convert_audio_to_wav(uploaded_file, target_sr=16000):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".original") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Load with pydub (auto-detects file type)
    audio = AudioSegment.from_file(tmp_path)
    audio = audio.set_channels(1).set_frame_rate(target_sr)

    # Export to WAV
    wav_path = tmp_path + ".wav"
    audio.export(wav_path, format="wav")
    return wav_path

# Simple language lookup for display
LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "zh-cn": "Chinese",
    "ja": "Japanese",
    "ar": "Arabic"
}
