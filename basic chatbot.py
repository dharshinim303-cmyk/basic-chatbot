import datetime

def show_help():
    print("\nYou can try asking:")
    print("- hello")
    print("- how are you")
    print("- what is your name")
    print("- time")
    print("- date")
    print("- help")
    print("- bye\n")

def chatbot():
    print("Chatbot: Hello! Welcome to CodeAlpha Chatbot 🤖")
    user_name = input("Chatbot: What's your name? \nYou: ")

    print(f"Chatbot: Nice to meet you, {user_name}!")
    print("Chatbot: Type 'help' to see what I can do.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print(f"Chatbot: Hi {user_name}! 😊")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks for asking!")

        elif user_input == "what is your name":
            print("Chatbot: I am a simple rule-based chatbot.")

        elif user_input == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Chatbot: Current time is", current_time)

        elif user_input == "date":
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print("Chatbot: Today's date is", current_date)

        elif user_input == "help":
            show_help()

        elif user_input == "bye":
            print(f"Chatbot: Goodbye {user_name}! Have a great day 👋")
            break

        else:
            print("Chatbot: Sorry, I didn't understand that. Type 'help'.")

# Run the chatbot
chatbot()
