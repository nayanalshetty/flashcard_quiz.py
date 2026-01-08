print("📚 ===== Flashcard Quiz App ===== 📚")

# Questions stored as dictionary
quiz = {
    "What is the capital of India?": {
        "a": "Mumbai",
        "b": "New Delhi",
        "c": "Kolkata",
        "d": "Chennai",
        "answer": "b"
    },
    "Which language is used for web development?": {
        "a": "Python",
        "b": "Java",
        "c": "HTML",
        "d": "C",
        "answer": "c"
    },
    "What is 5 + 3?": {
        "a": "5",
        "b": "10",
        "c": "8",
        "d": "9",
        "answer": "c"
    },
    "Who is the father of Computer?": {
        "a": "Charles Babbage",
        "b": "Alan Turing",
        "c": "Bill Gates",
        "d": "Steve Jobs",
        "answer": "a"
    }
}

score = 0

for q, options in quiz.items():
    print("\n🧠", q)
    print("a)", options["a"])
    print("b)", options["b"])
    print("c)", options["c"])
    print("d)", options["d"])

    user_ans = input("Your answer (a/b/c/d): ").lower()

    if user_ans == options["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is:", options["answer"])

print("\n🎯 ===== Quiz Finished =====")
print("Your Score:", score, "/", len(quiz))

if score == len(quiz):
    print("🏆 Excellent!")
elif score >= 2:
    print("👍 Good Job!")
else:
    print("📘 Keep Practicing!")
