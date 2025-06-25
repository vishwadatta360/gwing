import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10 # You can adjust this for difficulty

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue # Skip to the next iteration of the loop

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break # Exit the loop, as the guess is correct
    else: # This 'else' block executes if the while loop completes without a 'break'
        print(f"\nSorry, you ran out of attempts! The secret number was {secret_number}.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game() # Recursively call the function to play again
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    number_guessing_game()
