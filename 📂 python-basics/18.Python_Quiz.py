questions = ("What is the capital of France?",
             "What is 5 + 7?",
             "Which planet is known as the Red Planet?",
             )
options = (("A. Paris","B. England","C. India","D. South Korea",),
           ("A. 10","B. 11","C. 89","D. 12",),
           ("A. Mars","B. Earth","C. Moon","D. Venus",),
           )
answers = ("A", "D", "A",)
score = 0
question_number = 0
guesses = []
print("Welcome to Python Quiz Game!....")


for question in questions:
    print(question)
    for option in options[question_number]:
        print(option)
    guess = str(input("Enter your guess: "))
    guesses.append(guess)
    if guess == answers[question_number]:
        score =+1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_number]} is the correct answer.")
    question_number += 1
score = int(score / len(questions) * 100)
print(f"Your score is {score}")
