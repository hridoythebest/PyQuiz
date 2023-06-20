# This is a simple quiz game in Python

# Define some questions and answers as a list of tuples
questions = [
    ("What is the capital of Bangladesh?", "Dhaka"),
    ("What is the largest animal in the world?", "Blue whale"),
    ("Who is the author of Harry Potter?", "J.K. Rowling"),
    ("How many continents are there?", "Seven"),
    ("What is the smallest planet in the solar system?", "Mercury")
]

# Initialize a score variable to keep track of correct answers
score = 0

# Loop through each question and answer pair
for question, answer in questions:
    # Print the question and ask for user input
    print(question)
    user_answer = input("Your answer: ")

    # Check if the user answer matches the correct answer
    if user_answer.lower() == answer.lower():
        # If yes, print a positive feedback and increment the score
        print("Correct!")
        score += 1
    else:
        # If no, print a negative feedback and the correct answer
        print("Wrong!")
        print("The correct answer is:", answer)

    # Print a blank line for spacing
    print()

# Print the final score and a message based on the score
print("Your final score is:", score)
if score == len(questions):
    print("You aced the quiz!")
elif score > len(questions) // 2:
    print("You did well!")
else:
    print("You need to study more!")
