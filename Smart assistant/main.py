import speech_recognition as sr
import pyttsx3
from intents import intents
from tasks import get_time, open_website, add_reminder

# Voice engine setup
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("API unavailable or speech service down.")
        return ""

def match_intent(user_input):
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return intent
    return None

def assistant():
    speak("Smart Assistant is online. Say 'exit' anytime to quit.")

    while True:
        user_input = listen()
        if not user_input:
            continue

        intent = match_intent(user_input)

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
            reminder_text = listen()
            if reminder_text:
                speak(add_reminder(reminder_text))
        elif intent == "exit":
            speak(intents[intent]["response"])
            break
        else:
            speak("Sorry, I didn't get that.")

if __name__ == "__main__":
    assistant()
