import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load audio file
audio_file_path = "sample_audio.wav"  # <-- Replace with your file name

with sr.AudioFile(audio_file_path) as source:
    print("🎙️ Listening to the audio...")
    audio = recognizer.record(source)

# Try transcription using Google
try:
    print("🔎 Transcribing using Google Web Speech API...")
    text = recognizer.recognize_google(audio)
    print("\n📝 Transcription Result:")
    print(text)
except sr.UnknownValueError:
    print("❌ Could not understand audio")
except sr.RequestError:
    print("⚠️ Google API unavailable, falling back to offline mode (Sphinx)...")
    try:
        text = recognizer.recognize_sphinx(audio)
        print("\n📝 Transcription Result (Offline):")
        print(text)
    except sr.UnknownValueError:
        print("❌ Could not understand audio even in offline mode")
