import random

def guess_the_number():
    # Define the range for the random number
    lower_bound = 1
    upper_bound = 90
    # Generate a random number within the specified range
    number_to_guess = random.randint(lower_bound, upper_bound)
    # Define the number of attempts the player has
    attempts = 5

    print(f"Welcome to the Guess the Number game!")
    print(f"I have selected a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts} attempts to guess the number.")

    # Start the guessing game
    for attempt in range(1, attempts + 1):
        # Get the player's guess
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Check if the guess is correct
        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempt} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        # Check if the player has used all attempts
        if attempt == attempts:
            print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

# Run the game
if __name__ == "__main__":
    guess_the_number()