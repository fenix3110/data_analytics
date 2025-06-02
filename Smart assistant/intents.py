# intents.py

intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "response": "Hello! I’m your smart assistant. How can I help you today?"
    },
    "time": {
        "patterns": ["what time", "tell me time", "current time"],
        "response": None  # Dynamic
    },
    "open_google": {
        "patterns": ["open google", "go to google"],
        "response": "Opening Google..."
    },
    "open_youtube": {
        "patterns": ["open youtube", "go to youtube"],
        "response": "Opening YouTube..."
    },
    "set_reminder": {
        "patterns": ["remind me", "set reminder"],
        "response": None  # Will depend on user input
    },
    "exit": {
        "patterns": ["bye", "exit", "quit"],
        "response": "Goodbye! Have a great day!"
    }
}
