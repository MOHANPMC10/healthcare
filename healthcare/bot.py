import random

# Function to greet the user


def greet():
    greetings = ["Hello! How can I assist you today?",
                 "Hi there! How can I help you?", "Welcome! How may I assist you?"]
    return random.choice(greetings)

# Function to provide a list of available services


def provide_services():
    services = ["1. Book an appointment",
                "2. Get health information", "3. Talk to a doctor", "4. Exit"]
    return "\n".join(services)

# Function to handle user input and provide appropriate responses


def healthcare_bot():
    print(greet())

    while True:
        print("Please select one of the following services:")
        print(provide_services())
        user_choice = input()

        if user_choice == "1":
            book_appointment()
        elif user_choice == "2":
            get_health_info()
        elif user_choice == "3":
            talk_to_doctor()
        elif user_choice == "4":
            print("Thank you for using the healthcare bot. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

# Function to handle booking an appointment


def book_appointment():
    print("Please provide your personal details to book an appointment.")
    name = input("Name: ")
    age = input("Age: ")
    date = input("Preferred date: ")
    time = input("Preferred time: ")

    print("Appointment booked! We look forward to seeing you on", date, "at", time)

# Function to provide health information


def get_health_info():
    print("What health information would you like to know?")
    # Add your own health-related questions and responses here

# Function to initiate a conversation with a doctor


def talk_to_doctor():
    print("Please wait while we connect you to a doctor.")
    # Add code to connect to a doctor or schedule a callback


# Run the healthcare bot
healthcare_bot()
