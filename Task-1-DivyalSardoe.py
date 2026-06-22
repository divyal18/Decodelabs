# Project 1: Rule-Based AI Chatbot
# Phase 1: Input
def get_input():
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    return clean_input
# Phase 2: (Dictionary)
responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just code, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "thanks": "You're welcome!"
}
# Phase 3: (Infinite Loop)
while True:
    user_input = get_input()

    # Exit Strategy
    if user_input == "exit":
        print("Chatbot: Session terminated. 👋")
        break   
    reply = responses.get(user_input, "I do not understand that yet.")
    print(f"Chatbot: {reply}")
