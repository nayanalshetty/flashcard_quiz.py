import random

print("🎮 ===== Rock, Paper, Scissors Game ===== 🎮")

user_score = 0
computer_score = 0

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "4":
        print("\n👋 Game Over!")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        break

    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice! Try again.")
        continue

    user_choice = int(choice)

    if user_choice == 1:
        user = "Rock"
    elif user_choice == 2:
        user = "Paper"
    else:
        user = "Scissors"

    computer = random.choice(["Rock", "Paper", "Scissors"])

    print("\nYou chose:", user)
    print("Computer chose:", computer)

    # Decide winner
    if user == computer:
        print("🤝 It's a Tie!")
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        print("✅ You Win this round!")
        user_score += 1
    else:
        print("❌ Computer Wins this round!")
        computer_score += 1

    print("\n📊 Current Score:")
    print("You:", user_score, "| Computer:", computer_score)
