''' This isn't my handwork as I used AI to generate this code. I just made some minor edits to the code.
    I hope to write my own code in the future. '''

# A simple multiple-choice quiz game written in Python.
# This program will run in your terminal.

def run_quiz(questions):
    """
    This function contains the main game logic.
    It takes a list of question dictionaries and manages the quiz flow.
    """
    score = 0
    
    # Loop through each question in our list
    for question in questions:
        # Display the question to the user
        print("\n" + question["question"])
        
        # Display the answer choices
        for key, value in question["options"].items():
            print(f"  {key}. {value}")
            
        # Get the user's answer and convert it to lowercase
        user_answer = input("Enter your answer (a, b, c, or d): ").lower()
        
        # Check if the user's answer is correct
        if user_answer == question["correct_answer"]:
            print("Correct! 🎉")
            score += 1  # Add a point to the score
        else:
            print(f"Incorrect. The correct answer was {question['correct_answer']}.")
    
    # Display the final score
    print("\n--- Quiz Finished! ---")
    print(f"You scored {score} out of {len(questions)}.")
    
    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        run_quiz(questions)  # Call the function again to restart the quiz
    else:
        print("Thanks for playing! Goodbye.")

# Define the quiz questions in a list of dictionaries.
# Each dictionary contains the question, options, and the correct answer.
quiz_questions = [
    {
        "question": "What keyword is used to define a function in Python?",
        "options": {
            "a": "func",
            "b": "define",
            "c": "def",
            "d": "function"
        },
        "correct_answer": "c"
    },
    {
        "question": "What is the capital of France?",
        "options": {
            "a": "London",
            "b": "Berlin",
            "c": "Paris",
            "d": "Rome"
        },
        "correct_answer": "c"
    },
    {
        "question": "Who directed the movie 'Pulp Fiction'?",
        "options": {
            "a": "Martin Scorsese",
            "b": "Quentin Tarantino",
            "c": "Christopher Nolan",
            "d": "Steven Spielberg"
        },
        "correct_answer": "b"
    },
    {
        "question": "Which of these is not a Python data type?",
        "options": {
            "a": "list",
            "b": "tuple",
            "c": "dictionary",
            "d": "array"
        },
        "correct_answer": "d"
    }
]

# Start the game by calling the main function
if __name__ == "__main__":
    run_quiz(quiz_questions)
