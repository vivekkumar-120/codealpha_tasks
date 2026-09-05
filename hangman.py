import random
import string

# List of 5 predefined words
words = [
    "computer",
    "programming",
    "hangman",
    "developer",
    "keyboard"
]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Store letters already guessed
guessed_letters = set()

# Maximum incorrect guesses
max_incorrect_guesses = 6
incorrect_guesses = 0

print("=================================")
print("          HANGMAN GAME")
print("=================================")

while incorrect_guesses < max_incorrect_guesses:

    # Display current progress
    print("\nWord:", " ".join(guessed_word))

    print(
        "Incorrect guesses remaining:",
        max_incorrect_guesses - incorrect_guesses
    )

    # Display guessed letters
    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: None")

    # Get input
    letter = input("Enter a letter: ").strip().lower()

    # Check if input is exactly one letter
    if len(letter) != 1 or letter not in string.ascii_lowercase:
        print("Invalid input! Please enter one letter.")
        continue

    # Check for repeated guess
    if letter in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    # Add letter to guessed letters
    guessed_letters.add(letter)

    # Check whether letter exists in the word
    if letter in word:

        print(f"Correct! '{letter}' is in the word.")

        # Reveal the letter
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter

    else:

        incorrect_guesses += 1

        print(f"Wrong! '{letter}' is not in the word.")

    # Check if the complete word has been guessed
    if "_" not in guessed_word:

        print("\n=================================")
        print("          YOU WON!")
        print("=================================")
        print("The word was:", word)

        break

else:

    # Player used all 6 incorrect guesses
    print("\n=================================")
    print("          GAME OVER!")
    print("=================================")
    print("The word was:", word)

