# tasks.py

import datetime
import webbrowser

reminders = []

def get_time():
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."

def open_website(site):
    if site == "google":
        webbrowser.open("https://www.google.com")
    elif site == "youtube":
        webbrowser.open("https://www.youtube.com")

def add_reminder(text):
    reminders.append(text)
    return f"Reminder noted: '{text}'"

def list_reminders():
    if reminders:
        return "Here are your reminders:\n" + "\n".join(reminders)
    return "You don’t have any reminders yet."
