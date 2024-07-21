import random

words = ["UMBRELLA", "TELESCOPE", "TELEVISION", "SMARTPHONE", "COMPUTER", "KEYBOARD"]
word = random.choice(words)

total_chances = 7
guessed_word = "-" * len(word)

print("The word has", len(word), "letters:", guessed_word)

while total_chances > 0:
    letter = input("Guess a letter: ").upper().strip()  # Trim any whitespace

    if len(letter) != 1:  # Ensure that only one letter is entered
        print("Please enter a single letter.")
        continue  # Ask for another input

    print(f"Guessed letter: {letter}")  # Debug: print the guessed letter

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
        print("Correct guess!", guessed_word)

        if guessed_word == word:
            print("Congratulations you win!!! The word was:", word)
            break  # Exit the loop if the player has guessed the word
    else:
        total_chances -= 1
        print("Incorrect guess")
        print(f"The remaining chances are: {total_chances}")

if total_chances == 0:
    print("Game Over")
    print("You Lose")
    print("All the chances are exhausted")
    print("The correct word is", word)