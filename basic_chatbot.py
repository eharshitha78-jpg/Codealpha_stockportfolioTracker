# CodeAlpha Python Programming Internship
# Task 4 - Basic Chatbot

print("================================")
print("          BASIC CHATBOT")
print("================================")
print("Type 'bye' to end the conversation.")

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I'm doing great! How are you?")

    elif user_input == "what is your name":
        print("Bot: I'm a simple Python chatbot.")

    elif user_input == "what can you do":
        print("Bot: I can respond to some basic messages.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")