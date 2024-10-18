# Define a simple chatbot
def chatbot():
    print("Hi! I'm your chatbot, ROBO KID. How can I assist you today?")
    
    while True:
        user_input = input("You: ").lower()  # Convert user input to lowercase for easier matching
        
        # Exit condition
        if "exit" in user_input or "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Respond to greetings
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        
        # Respond to questions about weather
        elif "weather" in user_input:
            print("Chatbot: I'm not sure about the weather, but I hope it's nice outside!")
        
        # Respond to questions about time
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {current_time}.")
        
        # Respond to questions about chatbot's identity
        elif "who are you" in user_input or "what are you" in user_input:
            print("Chatbot: I'm ROBO KID created to assist you.")
        
        # Default response if the input doesn't match any predefined rules
        else:
            print("Chatbot: Sorry, I don't understand that. Could you rephrase?")
            
# Start the chatbot
chatbot()
