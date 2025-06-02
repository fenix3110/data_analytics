import tkinter as tk
from tkinter import scrolledtext
from utils import match_intent, check_eligibility

class LoanChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Loan Eligibility Chatbot")

        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='disabled')
        self.chat_display.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

        # Entry widget
        self.user_input = tk.Entry(root, width=50)
        self.user_input.grid(column=0, row=1, padx=10, pady=10)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.respond)
        self.send_button.grid(column=1, row=1)

        self.awaiting_eligibility = False
        self.greet_user()

    def greet_user(self):
        self._display("🤖", "Hello! I’m LoanBot. Type your message below.")
    
    def _display(self, sender, message):
        self.chat_display['state'] = 'normal'
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display['state'] = 'disabled'
        self.chat_display.see(tk.END)

    def respond(self):
        user_msg = self.user_input.get()
        if not user_msg.strip():
            return
        
        self._display("You", user_msg)
        self.user_input.delete(0, tk.END)

        if self.awaiting_eligibility:
            parts = user_msg.split()
            numbers = [int(word) for word in parts if word.isdigit()]
            if len(numbers) >= 2:
                age, income = numbers[0], numbers[1]
                reply = check_eligibility(age, income)
                self._display("🤖", reply)
                self.awaiting_eligibility = False
            else:
                self._display("🤖", "Please enter both your age and income.")
        else:
            reply, intent = match_intent(user_msg)
            self._display("🤖", reply)
            if intent == "loan_query":
                self.awaiting_eligibility = True

if __name__ == "__main__":
    root = tk.Tk()
    app = LoanChatbotApp(root)
    root.mainloop()
