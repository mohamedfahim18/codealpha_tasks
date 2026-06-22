score = 0

print("PHISHING AWARENESS QUIZ")
print("-" * 30)

questions = [
    {
        "question": "Which is a sign of a phishing email?",
        "options": [
            "A. Urgent request for personal information",
            "B. Proper company domain",
            "C. Verified sender",
            "D. Secure website"
        ],
        "answer": "A"
    },
    {
        "question": "What should you check before clicking a link?",
        "options": [
            "A. Font style",
            "B. URL destination",
            "C. Email color",
            "D. Attachment size"
        ],
        "answer": "B"
    },
    {
        "question": "HTTPS indicates:",
        "options": [
            "A. Secure communication",
            "B. Virus-free website",
            "C. Government website",
            "D. Fake website"
        ],
        "answer": "A"
    }
]

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Your Answer: ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nFinal Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! You understand phishing risks.")
elif score >= 2:
    print("Good Job!")
else:
    print("Learn more about phishing attacks.")