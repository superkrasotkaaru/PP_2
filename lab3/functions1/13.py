import random

def guess_the_number():
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    player_name = input()

    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")

    # Allow the player to make guesses
    for attempt in range(1, 7):
        guess = int(input())

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {attempt} guesses!")
            break

        if attempt == 6:
            print(f"Sorry, {player_name}, you've run out of attempts. The correct number was {secret_number}.")

# Run the game
guess_the_number()