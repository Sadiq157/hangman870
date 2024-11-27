import random as r

fruits = ("apple", "pear", "orange", "banana", "cherry")
random_word = r.choice(fruits)

def check_guess(guess, random_word):
    if guess in random_word:
        print(f"Good guess! {guess} is in the word")
        return True  # Return True to indicate the guess is correct
    else:
        print(f"Sorry, {guess} is not in the word")
        return False  # Return False if the guess is incorrect

def ask_for_input():
    while True:
        guess = input("Guess a letter: ").strip()  # Strip any extra spaces
        if not guess.isalpha():
            print("The letter must be alphabetical")
        elif len(guess) != 1:  # Ensure the input is only one letter
            print("Please guess only one letter.")
        else:
            return guess  # Return the valid guess

while True:
    guess = ask_for_input()  # Get the valid guess
    if check_guess(guess, random_word):  # If the guess is correct
        print("Congratulations! You guessed the correct letter!")
        break  # Exit the loop and stop the game
