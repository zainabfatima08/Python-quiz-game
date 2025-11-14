import random
import os


# High Score Store

def load_high_score():
    if os.path.exists("highscore.txt"):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read().strip() or "0")
        except ValueError:
            return 0
    return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))


# Quiz Questions

quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which programming language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Elon Musk", "B. Guido van Rossum", "C. Bill Gates", "D. Mark Zuckerberg"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Print Unit"],
        "answer": "B"
    }
]


random.shuffle(quiz)

score = 0
high_score = load_high_score()

print("======== *QUIZ GAME* ========")

# Quiz Loop

for q in quiz:
    print("\n" + q["question"])
    options = q["options"][:]
    random.shuffle(options)

    for opt in options:
        print(opt)

    # Input
    while True:
        answer = input("Enter your answer (A, B, C, D): ").strip().upper()
        if answer in ("A", "B", "C", "D"):
            break
        print("Invalid option. Please enter A, B, C, or D.")

    # AnSwEr Check
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        correct_text = next(o for o in q["options"] if o.startswith(q["answer"]))
        print(f"Oopsss Wrong! The correct answer is {correct_text}")


# Final Score & Percentage

percent = (score / len(quiz)) * 100
print(f"\nYour score: {score}/{len(quiz)} ({percent:.1f}%)")


# Feedback 

if percent >= 90:
    feedback = " You Rocked"
elif percent >= 70:
    feedback = "bohat khoob!"
elif percent >= 50:
    feedback = "Bas sahi hai"
else:
    feedback = " Parhai pa dihan doo "

print(f"Feedback: {feedback}")


# High Score Check

if score > high_score:
    print("New high score!")
    save_high_score(score)
else:
    print(f"High score: {high_score}")


    
