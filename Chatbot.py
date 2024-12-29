#BASIC CHATBOT
def simple_chatbot():
    print("Welcome to the SIMPLE CHATBOT")
    print("Types ___________")
    while True:
        user_type = input("You : ")

        if user_type == "bye":
            print("Chatbot : Goodbye!Have a nice day")
            break
        elif user_type == "hi":
            print("Chatbot : Hello! How can I help you")
        elif user_type == "hello":
            print("Chatbot : Hi! What can i help you")
        elif user_type == "how are you":
            print("Chatbot : I am just a program!I am here to assit you")
        elif user_type == "what is your name":
            print("Chatbot : I am chatbot! Your virtual asistant")
simple_chatbot()