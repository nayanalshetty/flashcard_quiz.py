import random

# List of words
words = ["python", "computer", "student", "program", "hangman"]

# Choose a random word
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 WELCOME TO HANGMAN GAME 🎮")
print("Guess the word letter by letter")
print("You have", attempts, "attempts\n")

while attempts > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts, "\n")
    else:
        print("Good guess!\n")

if attempts == 0:
    print("😢 Game Over! The word was:", secret_word)
