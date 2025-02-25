FEEDBACK_FILE = "Users_database/customer_feedback.txt"

def send_feedback(username):
    """Allows customers to send feedback."""
    
    feedback = input("\nEnter your feedback: ").strip()
    
    if feedback:
        try:
            with open(FEEDBACK_FILE, "a") as file:
                file.write(f"{username}: {feedback}\n")
            print("Thank you for your feedback!")
        except Exception as e:
            print(f"Error saving feedback: {e}")
    else:
        print("Feedback cannot be empty.")
        
    input("Press Enter to continue...")
    