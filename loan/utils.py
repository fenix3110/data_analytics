# utils.py

from responses import intents

def match_intent(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return data["response"], intent
    return "Sorry, I didn’t understand that. Could you rephrase?", None

def check_eligibility(age, income):
    try:
        age = int(age)
        income = int(income)

        if age < 21:
            return "You are too young to apply for a loan."
        elif income < 30000:
            return "Your income is below the minimum eligibility criteria."
        else:
            return "You seem eligible for a loan. Let's proceed!"
    except:
        return "Please enter valid numbers for age and income."
