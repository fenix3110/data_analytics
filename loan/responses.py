# responses.py

intents = {
    "greetings": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "response": "Hello! I'm your loan assistant. How can I help you today?"
    },
    "loan_query": {
        "patterns": ["loan", "eligible", "eligibility", "apply for loan", "can I get a loan"],
        "response": "Sure, I can help with that. Please tell me your age and monthly income."
    },
    "goodbye": {
        "patterns": ["bye", "exit", "quit", "see you", "goodbye"],
        "response": "Thanks for chatting. Have a great day!"
    }
}
