import tkinter as tk
import pyttsx3
import speech_recognition as sr
from intents import intents
from tasks import get_time, open_website, add_reminder

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    output.insert(tk.END, f"Assistant: {text}\n")
    engine.say(text)
    engine.runAndWait()

def listen_and_process():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        output.insert(tk.END, f"You: {command}\n")
        process_input(command)
    except:
        speak("Sorry, I didn't catch that.")

def match_intent(user_input):
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return intent
    return None

def process_input(command):
    intent = match_intent(command)
    if intent == "greeting":
        speak(intents[intent]["response"])
    elif intent == "time":
        speak(get_time())
    elif intent == "open_google":
        speak(intents[intent]["response"])
        open_website("google")
    elif intent == "open_youtube":
        speak(intents[intent]["response"])
        open_website("youtube")
    elif intent == "set_reminder":
        speak("What should I remind you?")
        with sr.Microphone() as source:
            audio = sr.Recognizer().listen(source)
            reminder = sr.Recognizer().recognize_google(audio)
            speak(add_reminder(reminder))
    elif intent == "exit":
        speak(intents[intent]["response"])
        window.destroy()
    else:
        speak("Sorry, I didn’t get that.")

# GUI Setup
window = tk.Tk()
window.title("Smart Assistant")
window.geometry("600x400")

output = tk.Text(window, height=20, width=70)
output.pack(pady=10)

listen_button = tk.Button(window, text="🎙 Speak", command=listen_and_process)
listen_button.pack()

window.mainloop()
