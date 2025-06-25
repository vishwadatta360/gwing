def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for option in question['options']:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}")

    print(f"\nYour final score is: {score}/{len(questions)}")


# List of questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "Which language is used to develop Android apps?",
        "options": ["A. Python", "B. Swift", "C. Java", "D. Ruby"],
        "answer": "C"
    }
]

# Run the quiz
run_quiz(quiz_questions)
