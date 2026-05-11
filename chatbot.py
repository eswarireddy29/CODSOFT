def chatbot():
    print("=" * 50)
    print("Welcome! I am CodBot - Your Personal Assistant!")
    print("=" * 50)
    print("You can ask me about:")
    print("  - Greetings")
    print("  - How I am doing")
    print("  - My name and who made me")
    print("  - Time and date")
    print("  - Jokes")
    print("  - Math (addition, subtraction)")
    print("  - General knowledge")
    print("  - Motivational quotes")
    print("  - Weather")
    print("  - Farewell")
    print("Type 'quit' to exit")
    print("=" * 50 + "\n")

    while True:
        user_input = input("You: ").strip().lower()

        # Empty input check
        if user_input == "":
            print("Chatbot: Please type something! I am here to help!\n")

        # Quit
        elif user_input in ["quit", "exit", "bye", "goodbye"]:
            print("Chatbot: Goodbye! It was nice talking to you! Have a wonderful day!\n")
            break

        # Greetings
        elif any(word in user_input for word in ["hello", "hi", "hey", "howdy", "greetings"]):
            print("Chatbot: Hello there! Great to see you! How can I help you today?\n")

        # How are you
        elif any(word in user_input for word in ["how are you", "how do you do", "are you okay", "you good"]):
            print("Chatbot: I am doing absolutely fantastic! Thank you for asking! What about you?\n")

        # Name
        elif any(word in user_input for word in ["your name", "who are you", "what are you"]):
            print("Chatbot: I am CodBot! A simple chatbot built using Python as part of CodSoft Internship!\n")

        # Who made you
        elif any(word in user_input for word in ["who made you", "who created you", "who built you"]):
            print("Chatbot: I was created by an awesome intern as part of the CodSoft Internship program!\n")

        # Jokes
        elif any(word in user_input for word in ["joke", "funny", "laugh", "humor"]):
            print("Chatbot: Here is a joke for you!")
            print("Chatbot: Why don't scientists trust atoms?")
            print("Chatbot: Because they make up everything! 😄\n")

        # Time
        elif any(word in user_input for word in ["time", "what time", "current time"]):
            import datetime
            now = datetime.datetime.now()
            print(f"Chatbot: The current time is {now.strftime('%I:%M %p')}\n")

        # Date
        elif any(word in user_input for word in ["date", "today", "what day"]):
            import datetime
            now = datetime.datetime.now()
            print(f"Chatbot: Today is {now.strftime('%A, %B %d, %Y')}\n")

        # Math - Addition
        elif "add" in user_input or "addition" in user_input or "plus" in user_input:
            print("Chatbot: Sure! Please enter the first number: ", end="")
            num1 = float(input())
            print("Chatbot: Please enter the second number: ", end="")
            num2 = float(input())
            print(f"Chatbot: The answer is {num1 + num2}\n")

        # Math - Subtraction
        elif "subtract" in user_input or "minus" in user_input or "difference" in user_input:
            print("Chatbot: Sure! Please enter the first number: ", end="")
            num1 = float(input())
            print("Chatbot: Please enter the second number: ", end="")
            num2 = float(input())
            print(f"Chatbot: The answer is {num1 - num2}\n")

        # Math - Multiplication
        elif "multiply" in user_input or "multiplication" in user_input or "times" in user_input:
            print("Chatbot: Sure! Please enter the first number: ", end="")
            num1 = float(input())
            print("Chatbot: Please enter the second number: ", end="")
            num2 = float(input())
            print(f"Chatbot: The answer is {num1 * num2}\n")

        # Math - Division
        elif "divide" in user_input or "division" in user_input:
            print("Chatbot: Sure! Please enter the first number: ", end="")
            num1 = float(input())
            print("Chatbot: Please enter the second number: ", end="")
            num2 = float(input())
            if num2 == 0:
                print("Chatbot: Oops! Cannot divide by zero!\n")
            else:
                print(f"Chatbot: The answer is {num1 / num2}\n")

        # Weather
        elif any(word in user_input for word in ["weather", "temperature", "rain", "sunny", "climate"]):
            print("Chatbot: I don't have access to live weather data!")
            print("Chatbot: But I suggest checking Google Weather or Weather.com for accurate updates!\n")

        # Motivational quotes
        elif any(word in user_input for word in ["motivate", "motivation", "quote", "inspire", "inspiration"]):
            print("Chatbot: Here is a motivational quote for you!")
            print('Chatbot: "Believe you can and you\'re halfway there." - Theodore Roosevelt\n')

        # Capital cities
        elif "capital" in user_input and "india" in user_input:
            print("Chatbot: The capital of India is New Delhi!\n")

        elif "capital" in user_input and "usa" in user_input:
            print("Chatbot: The capital of USA is Washington D.C.!\n")

        elif "capital" in user_input and "uk" in user_input:
            print("Chatbot: The capital of UK is London!\n")

        # Python
        elif "python" in user_input:
            print("Chatbot: Python is an amazing programming language!")
            print("Chatbot: It is easy to learn and very powerful. You are already using it right now!\n")

        # Thank you
        elif any(word in user_input for word in ["thank", "thanks", "thank you"]):
            print("Chatbot: You are most welcome! Happy to help anytime!\n")

        # Age
        elif any(word in user_input for word in ["your age", "how old"]):
            print("Chatbot: I am just a few lines of Python code old! Age doesn't apply to me! 😄\n")

        # Help
        elif "help" in user_input:
            print("Chatbot: I can help you with:")
            print("  - Greetings and small talk")
            print("  - Telling jokes")
            print("  - Current time and date")
            print("  - Basic math (add, subtract, multiply, divide)")
            print("  - Motivational quotes")
            print("  - General knowledge questions")
            print("  - Weather information\n")

        # Default response
        else:
            print("Chatbot: I am sorry, I didn't understand that.")
            print("Chatbot: Type 'help' to see what I can do!\n")

chatbot()