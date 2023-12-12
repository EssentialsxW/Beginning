
import random

def guessing_game():
    target_number = random.randint(1, 100)
    previous_guess = None
    num_guesses = 0

    while True:
        guess = int(input("Enter your guess (1 to 100): "))

        if guess < 1 or guess > 100:
            print("OUT OF BOUNDS! Please guess a number between 1 and 100.")
            continue

        num_guesses += 1

        if guess == target_number:
            print(f"Congratulations! You've guessed the correct number in {num_guesses} guesses.")
            break

        if previous_guess is None:
            if abs(guess - target_number) <= 10:
                print("WARM!")
            else:
                print("COLD!")
        else:
            if abs(guess - target_number) < abs(previous_guess - target_number):
                print("WARMER!")
            else:
                print("COLDER!")

        previous_guess = guess

guessing_game()
