import random

# List of words
words = ["python", "computer", "programming", "hangman", "developer"]

# Select a random word
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("=== Welcome to Hangman ===")

while incorrect_guesses < max_guesses:
    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    print("Remaining guesses:", max_guesses - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\n💀 Game Over! The word was:", word)
