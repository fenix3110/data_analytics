# main.py

from utils import match_intent, check_eligibility

def chatbot():
    print("🤖 LoanBot: Hello! Type 'exit' anytime to quit.")
    user_name = input("🤖 What's your name? ")
    print(f"🤖 Hi {user_name}, how can I help you today?\n")

    awaiting_eligibility_info = False

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("🤖 LoanBot: Thank you for chatting. Goodbye!")
            break

        if awaiting_eligibility_info:
            # Expect something like: "Age 25 Income 45000"
            parts = user_input.split()
            numbers = [int(word) for word in parts if word.isdigit()]
            if len(numbers) >= 2:
                age, income = numbers[0], numbers[1]
                response = check_eligibility(age, income)
                print("🤖 LoanBot:", response)
                awaiting_eligibility_info = False
            else:
                print("🤖 LoanBot: Please enter both age and income.")

        else:
            response, intent = match_intent(user_input)
            print("🤖 LoanBot:", response)

            if intent == "loan_query":
                awaiting_eligibility_info = True

if __name__ == "__main__":
    chatbot()
